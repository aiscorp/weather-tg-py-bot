import os
import telebot
from telebot import types
# ----
from dbinstance import DBInstance
from weather_api import OpenWeather

# init instances
bot = telebot.TeleBot(os.environ["BOT_SECRET_KEY"], threaded=False)
ow = OpenWeather(os.environ["OPEN_WEATHER_SECRET_KEY"])
db = DBInstance()


def telegram_bot(req):
    # receive message from server
    if req.method == "POST":
        update = types.Update.de_json(req.get_json(force=True))
        # update = types.Update.de_json(req.get_data().decode('utf-8'))
        # update = types.Update.de_json(req.text)
        msg = update.message or update.edited_message

        # db.logs_add({
        #     u'username': msg.chat.username,
        #     u'chat.id': msg.chat.id,
        #     u'text': msg.text
        # })

        if msg and msg.text and msg.text[0] == '/':
            bot.send_message(msg.chat.id, "Тут будут обрабатываться команды")
        elif msg and msg.text:
            text = msg.text.lower()
            if text.find('киев') != -1:
                city = 'киев'
            elif text.find('москв') != -1:
                city = 'москва'
            elif text.find('балаших') != -1:
                city = 'балашиха'
            elif text.find('нью') != -1:
                city = 'нью йорк'
            elif text.find('лондон') != -1:
                city = 'лондон'
            else:
                city = 'hell'

            weather = ow.by_name(city)
            bot.send_message(msg.chat.id, f"{msg.chat.username}, {ow.str_now_emoji(weather)}")
        else:
            bot.send_message(msg.chat.id, f"{msg.chat.username}, не понимаю")
    return "OK"
