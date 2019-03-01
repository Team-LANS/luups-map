from flask import render_template, request, redirect

from luupsmap import app, Venue
from luupsmap.service import VenueService

venue_service = VenueService()


@app.route('/')
def index():
    venues = venue_service.find_all()
    return render_template('main.jinja2', venues=venues)


@app.route('/venues')
def venues():
    venues = venue_service.find_all()
    return render_template('venues/index.html', venues=venues)


@app.route('/venue/<venue_id>')
def view(venue_id):
    return render_template('venues/show.html', venue=VenueService.get(venue_id))
