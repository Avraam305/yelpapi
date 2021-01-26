import requests
import json
import pprint
from constants import yelp_key, url_yelp


headers = {
            'Authorization': 'Bearer %s' % yelp_key
          }

parameters = {
            'location': 'San Francisco, CA',
            'limit': 50,
            'term': 'vegan cafe'
            }

response = requests.get(url_yelp, headers=headers, params=parameters)
data = response.json()
pprint.pprint(data, indent=2)

with open("yelpdata.json", "w") as json_file:
    json.dump(data, json_file)
