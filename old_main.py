import os
import requests
import json
from types import SimpleNamespace

#https://python-telegram-bot.readthedocs.io/en/stable/
import telegram


from dbinstance import DBInstance

ow_token = token = os.environ["OPEN_WEATHER_SECRET_KEY"]


def telegram_bot(request):
    bot = telegram.Bot(token=os.environ["BOT_SECRET_KEY"])
    db = DBInstance()

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        message = update.message

        chat_id = update.message.chat.id
        user = update.message.chat.username

        weather = ow_get_weather_by_location()
        bot.sendMessage(chat_id=chat_id,
                        text=f"{user}, в Лондоне сейчас {(weather.temp - 273.15):.{1}f}℃, а влажность {weather.humidity:.{0}f}%")

        db.logs_add(message.to_dict())
    return "OK"


def ow_get_weather_by_location(lat=51.509865, lon=-0.118092):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=1&appid={ow_token}")
    if (res.status_code == 200):
        return parse(res.text).list[0].main
    pass


def parse(data):
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
