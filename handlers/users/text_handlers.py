from telebot.types import Message, ReplyKeyboardRemove
from keyboards.replay import generate_weather_button
from data.loader import bot
import requests
from datetime import datetime
import time


@bot.message_handler(regexp='☁☁ Weather ☁☁')
def reaction_to_weather(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Названия города ?',
                           reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, weather_func)


parameters = {
    'appid': '137d62f3c460fac41edca5930e84af7c',
    'units': 'metric',
    'lang': 'ru'
}

def weather_func(message: Message):
    chat_id = message.chat.id
    city = message.text
    try:
        parameters['q'] = city
        data = requests.get('https://api.openweathermap.org/data/2.5/weather', parameters).json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        wind = data['wind']['speed']
        timezone = data['timezone']
        sunrise = datetime.utcfromtimestamp(data['sys']['sunrise'] + timezone).strftime('%H:%M:%S')
        sunset = datetime.utcfromtimestamp(data['sys']['sunset'] + timezone).strftime('%H:%M:%S')
        now = datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')

        bot.send_message(chat_id, f'''В городе {city} сейчас {description},
Температура: {temp} °C,
Скорость ветра: {wind} м/с,
Расвет: {sunrise},
Закат: {sunset},
Время: {now}''')
        # bot.send_message(chat_id, f'Температура: {temp} °C')
        # bot.send_message(chat_id,f'Скорость ветра: {wind} м/с')
        # bot.send_message(chat_id,f'Расвет: {sunrise}')
        # bot.send_message(chat_id,f'Закат: {sunset}')
        # bot.send_message(chat_id,f'Время: {now}')

        bot.send_message(chat_id,'Что вам еще найти?',
                         reply_markup=generate_weather_button() )

    except:
        bot.send_message(chat_id, 'Название города не корректно!',
                         reply_markup=generate_weather_button())
