from flask import render_template

from luupsmap import app


@app.route('/')
def index():
    return render_template('main.html')
