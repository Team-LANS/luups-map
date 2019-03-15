from flask import render_template, redirect, url_for

from luupsmap import app
from luupsmap.forms import LoginForm
from luupsmap.service import VenueService

venue_service = VenueService()


@app.route('/', methods=['GET'])
def index():
    venues_ = venue_service.find_all()
    form = LoginForm()
    return render_template('main.html', venues=venues_, form=form)


@app.route('/', methods=['POST'])
def todo():
    # TODO adapt this section
    venues_ = venue_service.find_all()
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index', _anchor='none'))
    return render_template('main.html', venues=venues_, form=form)


@app.route('/<int:venue_id>', methods=['GET'])
def show_details(venue_id):
    return render_template('details.html', venue=venue_service.get(venue_id))
