import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home Page!</h1>'

@app.route('/examples')
def examples():
    return '<h1>Example Personas</h1>'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)