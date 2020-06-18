import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)