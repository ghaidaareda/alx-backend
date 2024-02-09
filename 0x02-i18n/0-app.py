#!/usr/bin/env python3
"""
basic app
"""
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello():
    """ basic  route for / endpoint """
    return render_template("0-index.html")
