from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_weather_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='☁☁ Weather ☁☁')
    markup.add(btn)
    return markup
