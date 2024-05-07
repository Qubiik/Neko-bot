"""
 _____
/  __ \
| /  \/ ___  _ __  ___ _   _
| |    / _ \| '_ \/ __| | | |
| \__/\ (_) | | | \__ \ |_| |
 \____/\___/|_| |_|___/\__, |
                        __/ |
                       |___/
©Consy 2024
"""

import telebot
import random
from telebot import types

bot = telebot.TeleBot("6990833167:AAFR6aZEDl78W5wttJhT84NT1LbyzEQPwRI", parse_mode=None)

@bot.message_handler(commands=['neko'])
def neko(message):
    image = open("neko/" + str(random.randint(0, 231)) + ".jpg", "rb")
    bot.send_photo(message.chat.id, image)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Neko")
    btn2 = types.KeyboardButton("About")
    markup.add(btn1, btn2)
    bot.reply_to(message, "Command: \n/neko - send neko image", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def button(message):
    if(message.text == "Neko"):
        image = open("neko/" + str(random.randint(0, 231)) + ".jpg", "rb")
        bot.send_photo(message.chat.id, image)
    elif(message.text == "About"):
        bot.reply_to(message, "Discord: cons_y\nTelegram: @cons_y")

bot.polling(none_stop=True)
