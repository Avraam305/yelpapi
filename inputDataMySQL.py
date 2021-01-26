import pymysql
import json
from constants import db_host, db_password, db_user, db_name


json_data = open("yelpdata.json").read()
json_obj = json.loads(json_data)
json_data2 = json_obj["businesses"]
print(type(json_data2))

con = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)
cursor = con.cursor()

for item in json_data2:
    name = item.get("name")
    address = item.get("location").get("address1")
    state = item.get("location").get("state")
    city = item.get("location").get("city")
    latitude = item.get("coordinates").get("latitude")
    longitude = item.get("coordinates").get("longitude")
    stars = item.get("rating")
    postal_code = item.get("location").get("zip_code")
    phone = item.get("phone")
    cursor.execute("insert into businessinfotable(name,phone,stars,address,state,city,postal_code,latitude,longitude) "
                   "value(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (name, phone, stars, address, state, city, postal_code, latitude, longitude,))


con.commit()
con.close()
