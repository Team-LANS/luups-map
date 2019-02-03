"""
Fetches opening hours based on the place ID

Example:
    $ python hours.py 'ChIJ8_JZQZAHbUcRN4m3aYR7DqY'

"""

import os
import sys

import googlemaps
from dotenv import load_dotenv, find_dotenv


def main():
    ids = list(sys.argv[1:])
    load_dotenv(find_dotenv())
    gmaps_api_key = os.getenv("GMAPS_API_KEY")
    client = googlemaps.Client(key=gmaps_api_key)
    for ids in ids:
        result = client.place(ids, fields=['opening_hours'])
        weekdays = result['result']['opening_hours']['weekday_text']
        text = ', '.join(weekdays)
        print("%s | %s" % (ids, text))


if __name__ == "__main__":
    main()
