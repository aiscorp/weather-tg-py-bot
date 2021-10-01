import os
#https://python-telegram-bot.readthedocs.io/en/stable/
import telegram

from core.dbinstance import DBInstance
from core.weather_api import OpenWeather

ow_token = os.environ["OPEN_WEATHER_SECRET_KEY"]


def telegram_bot(request):
    bot = telegram.Bot(token=os.environ["BOT_SECRET_KEY"])
    db = DBInstance()
    ow = OpenWeather(ow_token)

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        message = update.message

        chat_id = update.message.chat.id
        user = update.message.chat.username

        weather = ow.by_name('москва')
        bot.sendMessage(chat_id=chat_id,
                        text=f"{user}, {ow.str_now_emoji(weather)}")

        db.logs_add(message.to_dict())
    return "OK"