import requests
import geocoder
import dotenv
import os

latitude = geocoder.ip('me').latlng[0]
longitude = geocoder.ip('me').latlng[1]
loc = geocoder.ip("me").state
loc2 = geocoder.ip("me").country

loc1 = geocoder.ip("me").city
print(loc, loc1, loc2)
print(latitude, longitude)

dotenv_load = dotenv.load_dotenv("apis.env")
x_rapid_api_forcast9 = os.environ.get("rapid_api_key_forcast9")
open_weather_one_call = os.environ.get("open_weather_one_call")


def wetter_api():
    url = f"https://forecast9.p.rapidapi.com/rapidapi/forecast/{latitude}/{longitude}/hourly/"

    headers = {
        "X-RapidAPI-Key": x_rapid_api_forcast9,
        "X-RapidAPI-Host": "forecast9.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    # print(response.json())
    return response.json()


def open_weather_api():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=hourly,daily&appid={open_weather_one_call}"

    response = requests.request("GET", url)

    # print(response.json())
    return response.json()


if __name__ == '__main__':
    pass
