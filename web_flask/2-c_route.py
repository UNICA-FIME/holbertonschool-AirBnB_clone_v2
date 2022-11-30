#!/usr/bin/python3
"""
This is a script that starts a Flask web application
"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
