#!/usr/bin/env python3
"""
basic app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, format_datetime
from datetime import datetime
from flask_babel import gettext


class Config:
    """Configuration class for the application."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale()-> str:
    """get locale"""
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)