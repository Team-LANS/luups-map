from flask import render_template, redirect, url_for, request

from luupsmap import app
from luupsmap.service import VenueService
from luupsmap.model import Type

venue_service = VenueService()


@app.route('/', methods=['GET'])
def index():
    venues_ = venue_service.find_all()
    return render_template('main.html', venues=venues_)


@app.route('/', methods=['POST'])
def filter():
    types = []
    if "food" in request.form.keys():
        types.append(Type.FOOD)
    if "drinks" in request.form.keys():
        types.append(Type.DRINK)
    if "entertainment" in request.form.keys():
        types.append(Type.TICKET)

    venues_ = venue_service.find_by_type(types)

    return render_template('main.html', venues=venues_)

@app.route('/<int:venue_id>', methods=['GET'])
def show_details(venue_id):
    return render_template('details.html', venue=venue_service.get(venue_id))
