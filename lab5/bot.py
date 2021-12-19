import telebot
import os
import config

bot = telebot.TeleBot(config.TOKEN)

cur_path = os.getcwd()

@bot.message_handler(commands=["start"])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = telebot.types.KeyboardButton('Привет, бот Дима!')
    markup.add(button)
    bot.send_message(message.chat.id, f'Привет, меня зовут бот-патриот Дима :)\nЯ умею:\n' \
    '1) отправлять флаг России\n2) отправлять герб России\n3) отправлять гимн', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def f(message):
    if message.text == 'Флаг':
        with open(os.path.join(cur_path, 'files\\flag.jpg'), 'rb') as img:
            bot.send_photo(message.chat.id, img)
    elif message.text == 'Герб':
        with open(os.path.join(cur_path, 'files\\emblem.jpg'), 'rb') as img:
            bot.send_photo(message.chat.id, img)
    elif message.text == 'Гимн':
        with open(os.path.join(cur_path, 'files\\гимн.mp3'), 'rb') as audio:
            bot.send_audio(message.chat.id, audio)
    else:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
        button1 = telebot.types.KeyboardButton('Флаг')
        button2 = telebot.types.KeyboardButton('Герб')
        button3 = telebot.types.KeyboardButton('Гимн')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Выбирете:', reply_markup=markup)

bot.infinity_polling()