# Test weather api
from weather_api import OpenWeather

ow = OpenWeather(token)  # type token

weather = ow.by_name('москва')

print(ow.str_now_emoji(weather))
