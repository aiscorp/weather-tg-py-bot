import traceback
import requests
import json
import logging
import flag

from types import SimpleNamespace


class OpenWeather:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(OpenWeather)
            return cls.instance
        return cls.instance

    def __init__(self, token, lang="ru"):
        try:
            self.token = token
            self.lang = lang
        except Exception as e:
            logging.error(traceback.format_exc())

    # https://openweathermap.org/current
    def by_geo_loc(self, lat=51.509865, lon=-0.118092):
        try:
            res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?"
                               f"lat={lat}&lon={lon}&cnt=1&appid={self.token}&lang={self.lang}&units=metric")
            if res.status_code == 200:
                return self.parse(res.text)
        except Exception as e:
            logging.error(traceback.format_exc())

    def by_name(self, name=u"Лондон", country=None):
        try:
            country_code = "" if country is None else f",{country}"
            res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?"
                               f"q={name}{country_code}&appid={self.token}&lang={self.lang}&units=metric")
            if res.status_code == 200:
                return self.parse(res.text)
        except Exception as e:
            logging.error(traceback.format_exc())

    # https://openweathermap.org/api/geocoding-api
    def geo_by_name(self, name=u"London", country=None):
        try:
            limit = 3  # number of given results
            country_code = "" if country is None else f",{country}"
            res = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?"
                               f"q={name}{country_code}&limit={limit}&appid={self.token}")
            if res.status_code == 200:
                return self.parse(res.text)
        except Exception as e:
            logging.error(traceback.format_exc())

    @staticmethod
    def parse(data):
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    @staticmethod
    def str_now(weather_response):
        w = weather_response
        return f"в городе\xa0{w.name}{flag.flag(w.sys.country)} сейчас {w.weather[0].description}, температура {w.main.temp:.{1}f}℃, " \
               f"давление {w.main.pressure / 1.333:.{0}f} мм рт.ст., влажность {w.main.humidity :.{0}f}%, " \
               f"скорость ветра {w.wind.speed:.{2}f} м/с, облачность {w.clouds.all}%"

    @staticmethod
    def str_now_emoji(weather_response):
        w = weather_response
        clouds = '⛅'
        humidity = '💧'
        rain = '☔'
        snow = '❄'
        temp = '❄' if w.main.temp < 5 else '☀'
        wind = '🚩'
        pressure = '🎈'
        return f"в городе\xa0{w.name}{flag.flag(w.sys.country)} сейчас {w.weather[0].description},  " \
               f"{temp}\xa0{w.main.temp:.{1}f}℃,  " \
               f"{pressure}{w.main.pressure / 1.333:.{0}f} мм рт.ст.,  " \
               f"{humidity}{w.main.humidity :.{0}f}%,  " \
               f"{wind}{w.wind.speed:.{2}f} м/с,  " \
               f"{clouds}\xa0{w.clouds.all}%"


# by_geo_loc() and by_name() response example
# {
#   "coord": {
#     "lon": -122.08,
#     "lat": 37.39
#   },
#   "weather": [
#     {
#       "id": 800,
#       "main": "Clear",
#       "description": "clear sky",
#       "icon": "01d"
#     }
#   ],
#   "base": "stations",
#   "main": {
#     "temp": 282.55,
#     "feels_like": 281.86,
#     "temp_min": 280.37,
#     "temp_max": 284.26,
#     "pressure": 1023,
#     "humidity": 100
#   },
#   "visibility": 16093,
#   "wind": {
#     "speed": 1.5,
#     "deg": 350
#   },
#   "clouds": {
#     "all": 1
#   },
#   "dt": 1560350645,
#   "sys": {
#     "type": 1,
#     "id": 5122,
#     "message": 0.0139,
#     "country": "US",
#     "sunrise": 1560343627,
#     "sunset": 1560396563
#   },
#   "timezone": -25200,
#   "id": 420006353,
#   "name": "Mountain View",
#   "cod": 200
#   }

# geo_by_name() response example
# [
#   {
#     "name": "London",
#     "local_names": {
#       ...
#       "ru": "Лондон",
#       ...
#     },
#     "lat": 51.5085,
#     "lon": -0.1257,
#     "country": "GB"
#   },
#   {
#     "name": "London",
#     "local_names": {
#       ...
#       "ru": "Лондон",
#       ...
#     },
#     "lat": 42.9834,
#     "lon": -81.233,
#     "country": "CA"
#   },
#   ...
# ]
