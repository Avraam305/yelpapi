import pymysql
import json
from constants import db_host, db_password, db_user, db_name, google_key, url_yelp, headers, parameters
import urllib.parse
import requests
from types import SimpleNamespace


response = requests.get(url_yelp, headers=headers, params=parameters)
data = response.json()
json_data2 = data["businesses"]

con = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)
cursor = con.cursor()

for item in json_data2:
    name = item.get("name")
    encode_name = (urllib.parse.quote(name))

    address = item.get("location").get("address1")
    state = item.get("location").get("state")
    city = item.get("location").get("city")
    latitude = item.get("coordinates").get("latitude")
    longitude = item.get("coordinates").get("longitude")
    stars = item.get("rating")
    postal_code = item.get("location").get("zip_code")
    phone = item.get("phone")
    url_google = (f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={encode_name}&'
                  'inputtype=textquery&fields=photos,formatted_address,name,opening_hours,rating&'
                  f'locationbias=circle:2000@{latitude},{longitude}&key={google_key}')
    response = requests.get(url_google)
    x = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
    rating = x.candidates[0].rating

    cursor.execute("insert into businessinfotable(name,phone,stars,address,state,city,postal_code,latitude,"
                   "longitude,googlerating) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (name, phone, stars, address, state, city, postal_code, latitude, longitude, rating))


con.commit()
con.close()
