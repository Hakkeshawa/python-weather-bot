import telebot
import requests
import json

key = '{your tg bot key}'
apikey = '{openweathermap api}'


bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! Type the name of your city')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message, f'Weather now: {data["main"]["temp"]} Celsius')


bot.polling(none_stop=True)