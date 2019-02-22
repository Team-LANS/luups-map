from flask import render_template, request, redirect

from luupsmap import app, Venue
from luupsmap.forms import VenueForm
from luupsmap.service import VenueService

venue_service = VenueService()


@app.route('/')
def index():
    venues = venue_service.find_all()
    return render_template('main.html', venues=venues)


@app.route('/venues')
def venues():
    venues = venue_service.find_all()
    return render_template('venues/index.html', venues=venues)


@app.route('/venue/new', methods=['GET', 'POST'])
def new_venue():
    if request.method == 'POST':
        form = VenueForm(request.form)
        venue = Venue(form_to_dict(form))
        venue_service.create(venue)
        return redirect("venues")

    form = VenueForm()
    return render_template('venues/edit.html', form=form)


def form_to_dict(form):
    return {
        'name': form.name.data,
        'description': 'NONE',
        'homepage': 'NONE',
        'email': 'NONE',
        'phone': 'NONE',
        'opening_hours': '7:00',
        'vouchers': [],
        'locations': []
    }
