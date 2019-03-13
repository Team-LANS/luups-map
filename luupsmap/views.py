from flask import render_template, request, redirect, flash, url_for

from luupsmap import app, Venue
from luupsmap.forms import LoginForm
from luupsmap.service import VenueService

venue_service = VenueService()


@app.route('/', methods=['GET', 'POST'])
def index():
    venues = venue_service.find_all()
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index', _anchor="none"))
    return render_template('main.jinja2', venues=venues, form=form)


@app.route('/venues')
def venues():
    venues = venue_service.find_all()
    return render_template('venues/index.html', venues=venues)


@app.route('/venue/<venue_id>')
def view(venue_id):
    return render_template('venues/show.html', venue=VenueService.get(venue_id))
