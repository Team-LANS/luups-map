from flask import render_template

from luupsmap import app
from luupsmap.service import VenueService

venue_service = VenueService()


@app.route('/')
def index():
    venues = venue_service.find_all()
    return render_template('main.html', venues=venues)
