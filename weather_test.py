# Test weather api
import requests
import json
from types import SimpleNamespace
from collections import namedtuple


def parse(data):
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


def req_weather():
    weather = ow_get_weather_by_location()
    return parse(weather["list"][0]["main"])


def ow_get_weather_by_location(lat=51.509865, lon=-0.118092):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=1&appid={ow_token}")
    if (res.status_code == 200):
        return parse(res.text)
    pass


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())


def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


res = ow_get_weather_by_location()

weather = res.list[0].main
print(f", в Лондоне сейчас {(weather.temp - 273.15):.{1}f}℃, а влажность {weather.humidity:.{0}f}%")

