import googlemaps

from luupsmap import app


# Store place details, which are used multiple times to save on requests to the Google API
class PlaceCache:
    places = {}

    def __init__(self):
        gmaps_api_key = app.config['GMAPS_API_KEY']
        self.gmaps = googlemaps.Client(key=gmaps_api_key)

    def get(self, name):
        if name not in self.places:
            self._fetch_place_details(name)
        # If no results were found on Google save empty result
        if name not in self.places:
            self.places[name] = []
        return self.places[name]

    def _fetch_place_details(self, name):
        gmaps_api_key = app.config['GMAPS_API_KEY']
        client = googlemaps.Client(key=gmaps_api_key)
        result = client.find_place(name, 'textquery',
                                   fields=['place_id'],
                                   location_bias='ipbias')
        for res in result['candidates']:
            place_id = res['place_id']
            place_data = client.place(place_id, fields=['website',
                                                        'international_phone_number',
                                                        'opening_hours',
                                                        'formatted_address',
                                                        'geometry'])
            self.places.setdefault(name, []).append(place_data['result'])
