import os
from flask import Flask, render_template, url_for, request
from flask_pymongo import PyMongo
from forms import CreatePersonaForm
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


@app.route('/add-persona', methods=['GET','POST'])
def add_persona():
    add_persona_form = CreatePersonaForm()
    persona = db.persona
    if request.method == 'POST':
        persona.insert_one(request.form.to_dict())
        return '<h1>Successfully added persona!</h1>'
    return render_template('add-persona.html', form=add_persona_form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)