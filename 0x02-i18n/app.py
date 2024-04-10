#!/usr/bin/env python3
"""Display current time"""
from flask import Flask, render_template
from flask_babel import Babel, gettext
from datetime import datetime
import pytz

app = Flask(__name__)
babel = Babel(app)


@babel.timezoneselector
def get_timezone():
    return 'UTC'


@app.route('/')
def home():
    now_utc = datetime.now(pytz.utc)
    user_timezone = pytz.timezone(get_timezone())
    local_time = now_utc.astimezone(user_timezone)
    formatted_time = local_time.strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=formatted_time)


if __name__ == "__main__":
    app.run(debug=True)
