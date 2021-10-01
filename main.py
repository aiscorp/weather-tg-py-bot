import os
import telebot
from telebot import types
# ----
from dbinstance import DBInstance
from weather_api import OpenWeather

# init instances
bot = telebot.TeleBot(os.environ["BOT_SECRET_KEY"])
ow = OpenWeather(os.environ["OPEN_WEATHER_SECRET_KEY"])
db = DBInstance()


def telegram_bot(req):
    # receive message from server
    update = types.Update.de_json(req.text)
    msg = update.message or update.edited_message

    if msg and msg.text and msg.text[0] == '/':
        weather = ow.by_name('лондон')
        bot.send_message(msg.chat.id, f"{msg.chat.username}, {ow.str_now_emoji(weather)}")
    elif msg and msg.text:
        weather = ow.by_name('киев')
        bot.send_message(msg.chat.id, f"{msg.chat.username}, {ow.str_now_emoji(weather)}")
        # route_command(message.text.lower(), message)
    else:
        bot.send_message(msg.chat.id, f"{msg.chat.username}, не понимаю")

    db.logs_add(msg)
