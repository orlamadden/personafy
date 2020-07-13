import os
from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

db = mongo.db

def get_persona(persona_id):
    return db.persona.find_one({"_id": ObjectId(persona_id)})

def registered_user(username):
    # function to find a registered username from the database
    user = db.user
    return user.find_one({"name": username})

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/public-personas')
def public_personas():
    """
    Reads all user personas from the database.

    View list of public user personas that have been created by
    registered users to Personafy.
    """
    personas = db.persona.find()

    dateCreated = personas
    
    occupation = [occ for occ in mongo.db.occupation.find({}, {"occupation_title": 1})]

    industry = [ind for ind in mongo.db.industry.find({}, {"industry_title": 1})]

    return render_template('public-personas.html',
    personas=personas, occupation=occupation, industry=industry)

@app.route('/view-persona/<persona_id>')
def view_persona(persona_id):
    """
    Read a single user persona from the database.

    View a single user persona that has been created by
    a registered user.
    """
    the_persona = db.persona.find_one({"_id": ObjectId(persona_id)})
    
    occupation_name = db.occupation.find_one({"_id": ObjectId(the_persona.get("occupation_title"))})
    
    industry_name = db.industry.find_one({"_id": ObjectId(the_persona.get("industry_title"))})

    return render_template('persona-card.html',
    persona=the_persona, persona_industry=industry_name, persona_occupation=occupation_name)

@app.route('/add-persona')
def add_persona():
    # add persona view
    db_occupation = db.occupation.find()
    db_industry = db.industry.find()

    return render_template('add-persona.html', occupation=db_occupation, industry=db_industry)

@app.route('/insert-persona', methods=['GET', 'POST'])
def insert_persona():
    """
    Create a user persona.
    
    Inserts all information from the form on the
    'Add Persona' page into the database.
    """
    persona = db.persona

    industry_title = request.form.get('industry')
    industry_id = db.industry.find_one({"industry_title": industry_title})["_id"]
    
    occupation_title = request.form.get('occupation')
    occupation_id = db.occupation.find_one({"occupation_title": occupation_title})["_id"]

    dateAndTime = datetime.now()
    
    if request.method == 'POST':
        persona.insert_one({
            'name': request.form.get('fname'),
            'age': request.form.get('age'),
            'bio': request.form.get('bio'),
            'profile': request.form.get('profile'),
            'occupation_title': occupation_id,
            'industry_title': industry_id,
            'goals': [request.form.get('goal-one'), request.form.get('goal-two'), request.form.get('goal-three')],
            'frustrations': [request.form.get('frustrations-one'), request.form.get('frustrations-two'), request.form.get('frustrations-three')],
            'creator': session['username'],
            'date_created': dateAndTime
        })
    
        return redirect(url_for('public_personas'))
    return render_template('add-persona.html', persona=persona, occupation=occupation, industry=industry)

@app.route('/edit_persona/<persona_id>')
def edit_persona(persona_id):
    the_persona = db.persona.find_one({'_id': ObjectId(persona_id)})
    
    occupation_name = db.occupation.find_one({"_id": ObjectId(the_persona.get("occupation_title"))})
    
    industry_name = db.industry.find_one({"_id": ObjectId(the_persona.get("industry_title"))})
    
    return render_template('edit-persona.html', persona=the_persona, occupation=db.occupation.find(), industry=db.industry.find(), occupation_title=occupation_name, industry_title=industry_name)

@app.route('/update_persona/<persona_id>', methods=['GET', 'POST'])
def update_persona(persona_id):
    persona = db.persona

    industry_title = request.form.get('industry')
    industry_id = db.industry.find_one({"industry_title": industry_title})["_id"]
    
    occupation_title = request.form.get('occupation')
    occupation_id = db.occupation.find_one({"occupation_title": occupation_title})["_id"]

    persona.update({'_id': ObjectId(persona_id)},
    {
        'name': request.form.get('fname'),
        'age': request.form.get('age'),
        'bio': request.form.get('bio'),
        'profile': request.form.get('profile'),
        'occupation_title': occupation_id,
        'industry_title': industry_id,
        'goals': [request.form.get('goal-one'), request.form.get('goal-two'), request.form.get('goal-three')],
        'frustrations': [request.form.get('frustrations-one'), request.form.get('frustrations-two'), request.form.get('frustrations-three')],
        'creator': session['username'],

    })
    
    return redirect(url_for('public_personas'))

@app.route('/delete_persona/<persona_id>')
def delete_persona(persona_id):
    persona = db.persona
    persona.remove({'_id': ObjectId(persona_id)})
    flash("Your persona has successfully been deleted.")
    
    return redirect(url_for('public_personas'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register a user.
    
    Checks the database if a username already exists, creates
    the user if the username does not exist already.
    """
    user = db.user
    if request.method == 'POST':
        new_username = request.form.get('username').lower()
        password = request.form.get('password')
        username_exists = user.find_one({'name': request.form.get('username')})

        # if username entry is not a letter or number, flash message
        for entry in new_username:
            if not entry.isalnum():
                flash("You can only use letters (a-z) and numbers (1-10) for your username")
                return redirect(url_for('register'))

        # checks database if username exists
        if username_exists is None:
            user.insert_one(
                {
                    'name' : new_username, 
                    'password': generate_password_hash(password)
                })
            session['username'] = new_username
            flash(f'Welcome {new_username}', 'success')
            return redirect(url_for('index', username=session["username"]))

        else:
            flash(f'Uh oh, that username already exists. Please try another username.', 'warning')
            return redirect(url_for('register'))
      
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    User Login. If Username not found in MongoDB db 'users', flash message
    and redirect user to try again on Login page. If password entered
    incorrect, flash relevant message and redirect to Login.
    """
    if request.method == 'POST':
        username = request.form.get('reg_username')
        password = request.form.get('user_password')
        reg_user = registered_user(username)
        
        # checks if username is registered is true
        if reg_user:
            """
            If registered user is true, check for hashed password
            against the registered username and flash welcome back 
            message when user successfully logs in.
            """
            if check_password_hash(reg_user["password"], password):
                flash(f"Welcome back {username}", "success")
                session['username'] = username
                return redirect(url_for('index', username=session["username"]))
                
            else:
                # Flash message on incorrect user login
                flash("There was a problem logging in. Check your username and password combination and please try again.")
                return redirect(url_for('login'))
        
        else:
            # Flash message when username does not exist
            flash(f"The username {username} does not exist. Please create an account.")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    """
    Logs out the user by clearing the session cache and redirects 
    user with flash message to index.
    """
    session.clear()
    flash('You have been logged out. Thank you!')
    return redirect(url_for('index'))

@app.route('/my_personas')
def my_personas():
    """
    Registered user's personas.
    
    A list of all the personas created by a particular user.
    """
    personas = db.persona.find()
    
    occupation = [occ for occ in mongo.db.occupation.find({}, {"occupation_title": 1})]

    industry = [ind for ind in mongo.db.industry.find({}, {"industry_title": 1})]

    return render_template('my-personas.html',
    personas=personas, occupation=occupation, industry=industry)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)