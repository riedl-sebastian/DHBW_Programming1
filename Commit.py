# import das Wetter ausgeben

import requests
import json

api_key = "derkey"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Stadt:  ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    temperature = y["temp"]
    pressure = y["pressure"]
    humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    print(" Temperature (in kelvin unit) = " +
                    str(temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(pressure) +
          "\n humidity (in percentage) = " +
                    str(humidity) +
          "\n description = " +
                    str(weather_description))
else:
    print(" Diese Stadt konnte nicht gefunden werden! ")