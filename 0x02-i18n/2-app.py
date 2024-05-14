#!/usr/bin/env python3
"""
basic app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, format_datetime
from datetime import datetime


class Config:
    """Configuration class for the application."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def hello():
    """ basic  route for / endpoint """
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])