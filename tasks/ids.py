"""
Retrieves Google place IDs from a given place name

Example:
    $ python ids.py 'mumok'

"""

import os
import sys

import googlemaps
from dotenv import load_dotenv, find_dotenv


def main():
    names = list(sys.argv[1:])
    load_dotenv(find_dotenv())
    gmaps_api_key = os.getenv("GMAPS_API_KEY")
    client = googlemaps.Client(key=gmaps_api_key)
    for name in names:
        result = client.find_place(name, 'textquery',
                                   fields=['place_id'],
                                   location_bias='ipbias')
        for res in result['candidates']:
            id = res['place_id']
            print("%s | %s" % (name, id))


if __name__ == "__main__":
    main()
