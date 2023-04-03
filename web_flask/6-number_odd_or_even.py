#!/usr/bin/python3
""" Create server with default main page """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """def index"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """def hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """def c <str:text>"""
    return "C " + text.replace('_', ' ')


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """def python [<str:text>]"""
    return "Python "+text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """def number <int:n>"""
    return str(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """def number_template <int:n>"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """def number_odd_or_even <int:n>"""
    even_or_odd = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, eod=even_or_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
