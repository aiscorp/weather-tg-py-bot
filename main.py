import os
import telegram
import requests
import json

ow_token = token=os.environ["OPEN_WEATHER_SECRET_KEY"]

def telegram_bot(request):
    bot = telegram.Bot(token=os.environ["BOT_SECRET_KEY"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
        weather = req_weather()
        bot.sendMessage(chat_id=chat_id, json.dumps(weather))
    return "okay"

def req_weather():
    weather = ow_get_weather_by_location()
    return weather["list"][0]["main"]

def ow_get_weather_by_location(lat=51.509865, lon=-0.118092):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=1&appid={ow_token}")
    if (res.status_code == 200):
        return res.json()
    pass
