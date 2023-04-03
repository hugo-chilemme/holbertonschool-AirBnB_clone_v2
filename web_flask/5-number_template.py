#!/usr/bin/python3
""" Create server with default main page """
from flask import Flask
from flask import render_template

app = Flask("hbnb_server")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ When the user access to the main page """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """ When the user access to the /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_c_is(text):
    """ When the user access to the /c/<text> """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_python_is(text="is cool"):
    """ When the user access to the /python/[<text>] """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ When the user access to the /number/<int:n> """
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number(n):
    """ When the user access to the /number_template/<int:n> """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
