import os
from flask import Flask, render_template, url_for, request
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

@app.route('/view-persona/<persona_id>', methods=["GET", "POST"])
def view_persona(persona_id):
    the_persona = db.persona.find_one({"_id": ObjectId(persona_id)})
    return render_template('persona-card.html',
    persona=the_persona)


@app.route('/add-persona', methods=['GET','POST'])
def add_persona():
    persona = db.persona
    if request.method == 'POST':
        persona.insert_one({
            'name': add_persona_form.name.data,
            'age': add_persona_form.age.data,
            'status': add_persona_form.status.data,
            'occupation': add_persona_form.occupation.data
        })
    
    

        return '<h1>Successfully added persona!</h1>'
    return render_template('add-persona.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)