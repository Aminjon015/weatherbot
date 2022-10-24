import requests
from datetime import datetime
import time

parameters = {
    'appid': '137d62f3c460fac41edca5930e84af7c',
    'units': 'metric',
    'lang': 'ru'
}


def weather():
    city = input('Введите город, в котором хотите узнать погоду:')
    parameters['q'] = city

    data = requests.get('https://api.openweathermap.org/data/2.5/weather', parameters).json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    wind = data['wind']['speed']
    time = data['timezone']
    now = datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')

    return data, temp, description, wind, time, now

print(weather())
