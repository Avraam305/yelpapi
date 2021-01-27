# yelpAPIrequest
For this project i used some simple libraries:
  * pip3 install requests
  * pip3 install pymysql

### We are making an API request to https://www.yelp.com/ 
### Yelp Documentation: https://www.yelp.com/developers/documentation/v3
### Google Documentation: https://developers.google.com/places/web-service/get-api-key


```python
#constants.py
# You can change this part of the code if you need to look for something else.
parameters = {
            'location': 'San Francisco, CA',
            'limit': 50,
            'term': 'vegan cafe'
            }
            
 # Example:
 
 parameters = {
            'location': 'Texas City, TX',
            'limit': 50,
            'term': 'cafe'
            }
```

[YelpRequestToDatabase.py](https://github.com/Avraam305/yelpapi/blob/main/YelpRequestToDatabase.py) sends a request to yelp.com, google.com/maps

then we parse this request using a loop and extract the required items into a database table with such fields:
 * name
 * phone
 * stars
 * address 
 * state 
 * city 
 * postal_code
 * latitude 
 * longitude
 * googlerating
  

``` python
# an example of parsing and loading data into a database
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
```

[constants.py](https://github.com/Avraam305/yelpapi/blob/main/constants.py) contains API keys which can be obtained from https://www.yelp.com/developers
and https://developers.google.com/places/web-service/get-api-key. Aso it contains your database connection information.



``` python

yelp_key = 'YOUR_YELP_API_KEY'
google_key = 'YOUR_GOOGLE_API_KEY'
url_yelp = 'https://api.yelp.com/v3/businesses/search'
db_password = 'YOUR_DATABASE_PASSWORD'
db_user = 'YOUR_DATABASE_USERNAME'
db_host = 'YOUR_DATABASE_HOST'
db_name = 'YOUR_DATABASE_NAME'

```


``` python
# database connection example

from constants import db_host, db_password, db_user, db_name

con = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)
cursor = con.cursor()


con.commit()
con.close()

```
### Code Result:
![ScreenShot](https://i.ibb.co/10ckwN4/photo-2021-01-27-15-14-28.jpg)
