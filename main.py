import os
import telebot
from telebot import types
# ----
from dbinstance import DBInstance
from weather_api import OpenWeather


def telegram_bot(**kwargs):
    print(f'Received: "{kwargs}"')
    # init instances
    bot = telebot.TeleBot(os.environ["BOT_SECRET_KEY"])
    ow = OpenWeather(os.environ["OPEN_WEATHER_SECRET_KEY"])
    db = DBInstance()

    # receive message from server
    update = types.Update.de_json(kwargs)
    msg = update.message or update.edited_message
    # log
    print(f'Received: "{kwargs}"')
    db.logs_add(msg.to_dict())

    if msg and msg.text and msg.text[0] == '/':
        weather = ow.by_name('лондон')
        bot.send_message(msg.chat.id, f"{msg.chat.username}, {ow.str_now_emoji(weather)}")
    elif msg and msg.text:
        weather = ow.by_name('киев')
        bot.send_message(msg.chat.id, f"{msg.chat.username}, {ow.str_now_emoji(weather)}")
        # route_command(message.text.lower(), message)
    else:
        bot.send_message(msg.chat.id, f"{msg.chat.username}, не понимаю")
