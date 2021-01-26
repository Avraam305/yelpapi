from inputdatamysql import json_data2
from constants import google_key
import urllib.parse
import requests
import pprint


for businesses_names in json_data2:
    names = businesses_names.get("name")
    latitude = businesses_names.get("coordinates").get("latitude")
    longitude = businesses_names.get("coordinates").get("longitude")
    encode_name = (urllib.parse.quote(names))
    url_google = (f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={encode_name}&'
                  'inputtype=textquery&fields=photos,formatted_address,name,opening_hours,rating&'
                  f'locationbias=circle:2000@{latitude},{longitude}&key={google_key}')

    response = requests.get(url_google)
    pprint.pprint(response.json(), indent=2)
