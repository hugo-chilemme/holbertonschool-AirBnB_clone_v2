'''script'''

from flask import flask

@app.route('/')
def hello():
    return 'Hello HBNB!'