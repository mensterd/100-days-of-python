import requests
from configparser import ConfigParser


# latlong.com
# https://jsonviewer.stack.hu
# a list of API's: https://apilist.fun/

ID_EINDHOVEN = 2756253
# ID_NIJMEGEN = 2750053
INI_FILE_NAME = "secrets.ini"

open_weather_base_url = "https://api.openweathermap.org/data/2.5/forecast"


# Read the initialization file for secret api key
configuration = ConfigParser()
configuration.read(INI_FILE_NAME)
open_weather_api_key = configuration.get(section="api_keys", option="open_weather_api_key")

# Set API parameters
# https://openweathermap.org/forecast5
parameters = {
    # "id": ID_EINDHOVEN,
    "lat": 51.436600,
    "lon": 5.478000,
    "units": "metric",
    "lang": "nl",
    "cnt": 5, # a number of timestamps, which will be returned in the API response.
    "appid": open_weather_api_key
}


# Make API call and fetch weather data for next <cnt> timestamps
response = requests.get(open_weather_base_url, params=parameters)
response.raise_for_status()
response = response.json()

umbrella = False
# Loop through the timestamps
for n in range(0, 5):
    # fetch the <id> and <description> of that timestamp
    date = response["list"][n]["dt_txt"]
    w_id = response["list"][n]["weather"][0]["id"]
    description = response["list"][n]["weather"][0]["description"]
    # if w_id < 700 then it is raining -> set umbrella
    if w_id < int(700):
        umbrella = True
    print(date, id, description)

if umbrella:
    print("Bring an Umbrella")


