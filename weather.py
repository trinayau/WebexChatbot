# Get weather data

import requests, json

url = "http://www.7timer.info/bin/api.pl?lon=0.085&lat=51.52&product=civillight&output=json"
response = requests.get(url)
data = json.loads(response.text) # loads json as a python dictionary 

data_today = data["dataseries"][0]
data_tomorrow = data["dataseries"][1]

# print today's forecast
print(data_today["weather"])
# print today's max temperature
print(data_today["temp2m"]["max"])
