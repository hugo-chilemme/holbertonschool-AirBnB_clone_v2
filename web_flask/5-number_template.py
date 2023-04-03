#!/usr/bin/python3
"""
    Create flask application instance (app)
"""
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
        Response to request main URL "/" or not in @app.route()
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
        Response to request URL "/hbnb" or "/hbnb/" in @app.route()
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """
        Response to request URL "c/<text>" in @app.route()
        display C follow by the value of text
    """
    new_text = escape(text).replace("_", " ")
    return f"C {new_text}"


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def Python_text(text):
    """
        Response to request URL "python/<text>" in @app.route()
        display Python follow by the value of text or 'is cool' if no text
    """
    new_text = escape(text).replace("_", " ")
    return f"Python {new_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
        Response to request URL "number/n" in @app.route()
        display "n is a number" only if n is an integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    """
        Display a HTML page only if n is an integer:
        h1 tag "Number: n" inside the tag BODY
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
