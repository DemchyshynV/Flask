from app import app
from flask import render_template

ss = False
users = ['Max', 'Kokos', 'Petia', 'Katia']


@app.route('/')
def hello_world():
    return render_template('index.html', boolean=ss, users=users)
