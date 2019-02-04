from flask import Flask

app = Flask(__name__)

import luupsmap.model.venue

import luupsmap.views

