import datetime as dt
import requests
import os
user_api = os.environ['current_weather_data']
# print('my id:',user_api)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY=input("enter name of city")
def kelvin_to_celcius_fahrenheit(kelvin):
    celsius = kelvin -273.15
    fahrenheit= celsius* (9/5) + 32
    return celsius,fahrenheit
url = BASE_URL + "appid=" + user_api + "&q=" + CITY
response =requests.get(url).json()
temp_kelvin =response['main']['temp']
temp_celsius,temp_fahrenheit =kelvin_to_celcius_fahrenheit(temp_kelvin)
feels_like_kelvin= response['main']['feels_like']
feels_like_celsius,feels_like_fahrenheit =kelvin_to_celcius_fahrenheit(feels_like_kelvin)
wind_speed=response['wind']['speed']
humidity= response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
print(f"Temperature in {CITY}:{temp_celsius:2f}C or {temp_fahrenheit:2f}F")
print(f"Temperature in {CITY}:feels_like:{feels_like_celsius:.2f}C or {feels_like_fahrenheit:2f}F")
print(f"Humidity in {CITY}:{humidity}%")
print(f"wind_speed in {CITY}:{wind_speed}m/s")
print(f"General weather in {CITY}:{description}")
print(f"sun rises in {CITY} at {sunrise_time} local time.")
print(f"sun sets in {CITY} at {sunset_time} local time.")