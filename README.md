# weather-tg-py-bot
Telegram bot on Python for weather forecasts with google functions deploy

## Deploy a Google Cloud Function:
```
gcloud functions deploy telegram_bot \
 --set-env-vars "BOT_SECRET_KEY=<>,OPEN_WEATHER_SECRET_KEY=<>" \
 --runtime python38 --trigger-http \
 --project=<>
```

## Set up Webhook URL using this API call:
```
curl "https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook?url=<URL>"
```

## Connect DB by articles:
````
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/firestore/cloud-client/snippets.py
https://cloud.google.com/docs/authentication/getting-started
````
