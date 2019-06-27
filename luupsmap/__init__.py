from flask import Flask

import os

from dotenv import load_dotenv, find_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from luupsmap.model import *

import luupsmap.views

import luupsmap.cli.data


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Venue': Venue, 'Location': Location, 'Interval': Interval}
