import os
from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_pymongo import PyMongo
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

def registered_user(username):
    user = db.user
    return user.find_one({"name": username})

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/public-personas')
def public_personas():
    return render_template('public-personas.html',
    personas=mongo.db.persona.find())

@app.route('/view-persona/<persona_id>')
def view_persona(persona_id):
    the_persona = db.persona.find_one({"_id": ObjectId(persona_id)})
    return render_template('persona-card.html',
    persona=the_persona)


@app.route('/add-persona', methods=['GET','POST'])
def add_persona():
    persona = db.persona
    occupation = db.occupation.find()
    industry = db.industry.find()
    if request.method == 'POST':
        persona.insert_one({
            'name': request.form.get('fname'),
            'age': request.form.get('age'),
            'bio': request.form.get('bio'),
            'profile': request.form.get('profile'),
            'occupation_title': request.form.get('occupation'),
            'industry_title': request.form.get('industry'),
            'goals': request.form.get('goals'),
            'frustrations': request.form.get('frustrations'),
            'creator': session['username']
        })
    
        return '<h1>Successfully added persona!</h1>'
    return render_template('add-persona.html', persona=persona, occupation=occupation, industry=industry)

@app.route('/edit_persona/<persona_id>')
def edit_persona(persona_id):
    the_persona = db.persona.find_one({'_id': ObjectId(persona_id)})
    all_occupation = db.occupation.find()
    all_industry = db.industry.find()
    return render_template('edit-persona.html', persona=the_persona, occupation=all_occupation, industry=all_industry)

@app.route('/update_persona/<persona_id>', methods=['GET', 'POST'])
def update_persona(persona_id):
    persona = db.persona
    persona.update({'_id': ObjectId(persona_id)},
    {
        'name': request.form.get('fname'),
        'age': request.form.get('age'),
        'bio': request.form.get('bio'),
        'occupation_title': request.form.get('occupation'),
        'industry_title': request.form.get('industry'),
        'goals': request.form.get('goals'),
        'frustrations': request.form.get('frustrations')
    })
    
    return redirect(url_for('public_personas'))

@app.route('/delete_persona/<persona_id>')
def delete_persona(persona_id):
    persona = db.persona
    persona.remove({'_id': ObjectId(persona_id)})
    return redirect(url_for('public_personas'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    user = db.user
    if request.method == 'POST':
        new_username = request.form.get('username').lower()
        password = request.form.get('password')
        username_exists = user.find_one({'name': request.form.get('username')})
        
        if username_exists is None:
            user.insert_one(
                {
                    'name' : new_username, 
                    'password': generate_password_hash(password)
                })
            session['username'] = new_username
            flash(f'Welcome {new_username}', 'success')
            return redirect(url_for('index', username=session["username"]))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('reg_username')
        password = request.form.get('user_password')
        reg_user = registered_user(username)

        if reg_user:
            if check_password_hash(reg_user["password"], password):
                flash(f"Welcome back {username}", "success")
                session['username'] = username
                return redirect(url_for('index', username=session["username"]))
                
            else:
                # Login validation
                flash(f"The password or username {username} does not exist and details do not match our records")
                return redirect(url_for('login'))
        
        else:
            flash(f"The username {username} does not exist")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

@app.route('/my_personas')
def my_personas():
    return render_template('my-personas.html',
    personas=mongo.db.persona.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)