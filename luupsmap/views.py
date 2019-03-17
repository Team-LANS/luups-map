from flask import render_template, redirect, url_for, request

from luupsmap import app
from luupsmap.service import VenueService
from luupsmap.model import Type, Tag

venue_service = VenueService()


@app.route('/', methods=['GET'])
def index():
    venues_ = venue_service.find_all()
    tags = [t.name.replace("_", " ").lower() for t in Tag]
    types = [t.name.lower() for t in Type]
    return render_template('main.html', venues=venues_, types=types, tags=tags)


@app.route('/', methods=['POST'])
def filter():
    types = []
    if "food" in request.form.keys():
        types.append(Type.FOOD)
    if "drink" in request.form.keys():
        types.append(Type.DRINK)
    if "ticket" in request.form.keys():
        types.append(Type.TICKET)

    venues_ = venue_service.find_by_type(types)
    tags = [t.name.replace("_", " ").lower() for t in Tag]
    types = [t.name.lower() for t in Type]
    return render_template('main.html', venues=venues_, types=types, tags=tags)


@app.route('/<int:venue_id>', methods=['GET'])
def show_details(venue_id):
    return render_template('details.html', venue=venue_service.get(venue_id))


def pretty_tag(tag):
    tag = tag.replace("_", " ")

