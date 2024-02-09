#!/usr/bin/env python3
"""
basic app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, format_datetime
from datetime import datetime 

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Configuration class for the application."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
@babel.localeselector
def get_locale():
        return request.accept_languages.best_match(Config.LANGUAGES, default=Config.BABEL_DEFAULT_LOCALE)
