#!/usr/bin/python3
""" Create server with default main page """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """def index"""
    return "Hello HBNB!"


@app.teardown_appcontext
def afterRequest(self):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """def states_list"""
    from models.state import State
    states = []
    for state in storage.all(State).values():
        states.append(state.to_dict())

    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
