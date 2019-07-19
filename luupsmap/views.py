from flask import render_template, redirect, url_for, request

from datetime import datetime

from luupsmap import app
from luupsmap.service import VenueService, LocationService
from luupsmap.model import Type, Tag
from luupsmap.dto import LocationSearchDto

venue_service = VenueService()
location_service = LocationService()


@app.route('/', methods=['GET'])
def index():
    venues_ = venue_service.find_all()
    tags = [(t.name.lower(), Tag.translation(t)) for t in Tag]
    types = [t.name.lower() for t in Type]
    return render_template('main.html', venues=venues_, types=types, tags=tags)


@app.route('/location', methods=['GET'])
def location():
    payload = request.get_json()
    locations = location_service.find_all(LocationSearchDto(payload))
    return  render_template('main.html')


@app.route('/', methods=['POST'])
def filter():
    types = [t for t in Type if t.name.lower() in request.form.keys()]
    tags = [t for t in Tag if "tag-" + t.name.lower() in request.form.keys()]
    time_string = request.form['time']
    if time_string == '':
        time = None
    else:
        time = datetime.strptime(time_string, "%H:%M %d-%m-%Y")

    venues = venue_service.filter_by(types, tags, time)
    tags = [(t.name.lower(), Tag.translation(t)) for t in Tag]
    types = [t.name.lower() for t in Type]
    return render_template('main.html', venues=venues, types=types, tags=tags)


@app.route('/<int:location_id>', methods=['GET'])
def show_details(location_id):
    location = location_service.get(location_id)
    return render_template('details.html', venue=venue_service.get(location.id_venue), location=location)


