# Load .env
import os

from dotenv import load_dotenv, find_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from luupsmap import app

load_dotenv(find_dotenv())

app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


