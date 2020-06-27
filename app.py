import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

db = mongo.db

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
            'occupation_title': request.form.get('occupation'),
            'industry_title': request.form.get('industry'),
            'goals': request.form.get('goals'),
            'frustrations': request.form.get('frustrations')
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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)