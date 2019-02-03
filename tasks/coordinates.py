"""
Fetches latitude and longitude for a list of addresses and prints them as tab separated list

Example:
    $ python coordinates.py 'Ybbstrasse 15-21, 1020 Wien' 'Baumgasse 35, 1030 Wien'

"""

import os
import sys

import googlemaps
from dotenv import load_dotenv, find_dotenv


def main():
    addresses = list(sys.argv[1:])
    load_dotenv(find_dotenv())
    gmaps_api_key = os.getenv("GMAPS_API_KEY")
    gmaps = googlemaps.Client(key=gmaps_api_key)
    for adress in addresses:
        geocode_result = gmaps.geocode(adress)
        for res in geocode_result:
            coords = res['geometry']['location']
            print("%s | %s | %s" % (adress, coords['lat'], coords['lng']))


if __name__ == "__main__":
    main()
