# yelpAPIrequest
For this project i used some simple libraries:
  * pip3 install requests
  * pip3 install pymysql

### We are making an API request to https://www.yelp.com/
### Documentation: https://www.yelp.com/developers/documentation/v3


```python
# yelpapirequest.py
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

yelpapirequest.py sends a request to yelp.com and loads it into a json file ([yelpdata.json](https://github.com/Avraam305/yelpapi/blob/main/yelpData.json))

then we parse this json file using a loop and extract the required items into a database table with such fields:
 * name
 * phone
 * stars
 * address 
 * state 
 * city 
 * postal_code
 * latitude 
 * longitude
  

``` python
# an example of parsing and loading data into a database
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
```

[constants.py](https://github.com/Avraam305/yelpapi/blob/main/constants.py) contains API keys which can be obtained from https://www.yelp.com/developers
and https://developers.google.com/places/web-service/get-api-key

``` python

yelp_key = 'YOUR_YELP_API_KEY'
google_key = 'YOUR_GOOGLE_API_KEY'
url_yelp = 'https://api.yelp.com/v3/businesses/search'
db_password = 'YOUR_DATABASE_PASSWORD'
db_user = 'YOUR_DATABASE_USERNAME'
db_host = 'YOUR_DATABASE_HOST'
db_name = 'YOUR_DATABASE_NAME'

```
