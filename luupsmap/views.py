from flask import render_template, redirect, url_for, request

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
def show_details():
    request_params = request.form.to_dict()
    venue_id = _get_key_by_value(request_params, 'Details anzeigen')
    venue = venue_service.get(int(venue_id))

    # TODO adapt this section
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index', _anchor='none'))

    return render_template('details.html', venue=venue)


@app.route('/venues')
def venues():
    venues = venue_service.find_all()
    return render_template('venues/index.html', venues=venues)


@app.route('/venue/<venue_id>')
def view(venue_id):
    return render_template('venues/show.html', venue=VenueService.get(venue_id))


def _get_key_by_value(dict_, value_):
    for key, value in dict_.items():
        if value == value_:
            return key
    else:
        return None
