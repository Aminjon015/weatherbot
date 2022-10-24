from data.loader import bot
from telebot.types import Message
from keyboards.replay import generate_weather_button

@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    text = f"""Здравствуйте {message.from_user.full_name}
Я могу показать погоду!"""
    bot.send_message(chat_id, text, reply_markup=generate_weather_button())
