import requests
from pprint import pprint

API_Key = '7979f56444190772c5e4433ea4ac22c2'

city = input("Enter a city:")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
