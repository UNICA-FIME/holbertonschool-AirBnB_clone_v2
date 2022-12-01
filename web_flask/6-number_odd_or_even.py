#!/usr/bin/python3
"""
This is a script that starts a Flask web application
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """The function returns the message we
    want to display in the user’s browser
    display: Hello HBNB!
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    The function returns the message we
    want to display in the user’s browser
    display: HBNB
    """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    The function returns the message we
    want to display in the user’s browser
    if input is c_fun return in display:
    c fun
    """
    c = list(text)
    str_1 = "".join([i if i != '_' else ' ' for i in c])
    return ("C %s" % str_1)


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    The function returns the message we
    want to display in the user’s browser
    if input is c_fun return in display:
    The default value of text is “is cool”
    """
    c = list(text)
    str_1 = "".join([i if i != '_' else ' ' for i in c])
    return ("Python %s" % str_1)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    The function returns the message we
    want to display in the user’s browser
    if input is c_fun return in display:
    n is a number” only if n is an integer
    """
    if type(n) is int:
        return ("%d is a number" % int(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    The function returns the message we
    want to display in the user’s browser
    if input is c_fun return in display:
    show number type int read file html
    use render_template.
    """
    if type(n) is int:
        return render_template('5-number.html', n=(n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    The function returns the message we
    want to display in the user’s browser
    if input is c_fun return in display:
    show number type int read file html
    use render_template whit if and else in jinja.
    """
    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
