import dbworker
import config
import telebot
from weather import weather_forecast
from functions import picture_path

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def greetings(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('Привет, бот Дима'))
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.START_STATE.value)
    bot.send_message(message.chat.id, 'Привет, меня зовут бот Дима, я могу отправлять прогноз погоды!', reply_markup=markup)

@bot.message_handler(func=lambda message:
int(dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE))) == config.States.START_STATE.value)
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('Геолокация', request_location=True))
    bot.send_message(message.chat.id, 'Отправь мне свою геолокацию или введи город!', reply_markup=markup)
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.LOCATION_STATE.value)

@bot.message_handler(content_types=["location"], func= lambda message:
int(dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE))) == config.States.LOCATION_STATE.value)
def location_geo(message):
    if message.location is not None:
        dbworker.set(dbworker.make_key(message.chat.id, config.States.LOCATION_STATE.value), 0)
        dbworker.set(dbworker.make_key(message.chat.id, 'longitude'), message.location.longitude)
        dbworker.set(dbworker.make_key(message.chat.id, 'latitude'), message.location.latitude)
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.DAY_STATE.value)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt1 = telebot.types.KeyboardButton('Сегодня')
        bt2 = telebot.types.KeyboardButton('Завтра')
        bt3 = telebot.types.KeyboardButton('Послезавтра')
        markup.add(bt1, bt2, bt3)
        bot.send_message(message.chat.id, 'Выберите день, на который хотите посмотреть погоду', reply_markup=markup)

@bot.message_handler(func=lambda message: 
int(dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE))) == config.States.LOCATION_STATE.value)
def location_city(message):
    if message.text:
        dbworker.set(dbworker.make_key(message.chat.id, config.States.LOCATION_STATE.value), 1)
        dbworker.set(dbworker.make_key(message.chat.id, 'city'), message.text)
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.DAY_STATE.value)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt1 = telebot.types.KeyboardButton('Сегодня')
        bt2 = telebot.types.KeyboardButton('Завтра')
        bt3 = telebot.types.KeyboardButton('Послезавтра')
        markup.add(bt1, bt2, bt3)
        bot.send_message(message.chat.id, 'Выберите день, на который хотите посмотреть погоду', reply_markup=markup)

@bot.message_handler(func=lambda message:
int(dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE))) == config.States.DAY_STATE.value)
def day(message):
    if message.text == 'Сегодня' or message.text == 'Завтра' or message.text == 'Послезавтра':
        if message.text == 'Сегодня':
            dbworker.set(dbworker.make_key(message.chat.id, config.States.DAY_STATE.value), 0)
        elif message.text == 'Завтра':
            dbworker.set(dbworker.make_key(message.chat.id, config.States.DAY_STATE.value), 1)
        else:
            dbworker.set(dbworker.make_key(message.chat.id, config.States.DAY_STATE.value), 2)
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.DETAIL_STATE.value)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt1 = telebot.types.KeyboardButton('Коротко')
        bt2 = telebot.types.KeyboardButton('Подробно')
        markup.add(bt1, bt2)
        bot.send_message(message.chat.id, 'Выберите краткий прогноз или полный', reply_markup=markup)
    else:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt1 = telebot.types.KeyboardButton('Сегодня')
        bt2 = telebot.types.KeyboardButton('Завтра')
        bt3 = telebot.types.KeyboardButton('Послезавтра')
        markup.add(bt1, bt2, bt3)
        bot.send_message(message.chat.id, 'Выберите день из списка ниже', reply_markup=markup)
    
@bot.message_handler(func=lambda message:
int(dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE))) == config.States.DETAIL_STATE.value)
def detail(message):
    if message.text == 'Коротко' or message.text == 'Подробно':
        if int(dbworker.get(dbworker.make_key(message.chat.id, config.States.LOCATION_STATE.value))):
            forecast = weather_forecast(dbworker.get(dbworker.make_key(message.chat.id, 'city')), 
            int(dbworker.get(dbworker.make_key(message.chat.id, config.States.DAY_STATE.value))))
        else:
            forecast = weather_forecast(dbworker.get(dbworker.make_key(message.chat.id, 'longitude')),
            dbworker.get(dbworker.make_key(message.chat.id, 'latitude')),
            int(dbworker.get(dbworker.make_key(message.chat.id, config.States.DAY_STATE.value))))
        if message.text == 'Коротко':
            res = {"погода:" : forecast['weather'][0]['description'], "температура:" : forecast['main']['temp'], 
            "ощущается:" : forecast['main']['feels_like']}
        else:
            res = {"погода:" : forecast['weather'][0]['description'], "температура:" : forecast['main']['temp'], 
            "ощущается:" : forecast['main']['feels_like'], "минимальная температура:" : forecast['main']['temp_min'], 
            "максимальная температура:" : forecast['main']['temp_max'], "атмосферное давление:" : forecast['main']['pressure']}
        path = picture_path(res['погода:'])
        result = ''
        for k, v in res.items():
            result += k + ' ' + str(v) + '\n'
        with open(path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, result)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        markup.add(telebot.types.KeyboardButton('Да'), telebot.types.KeyboardButton('Нет'))
        bot.send_message(message.chat.id, 'Желаете ли посмотреть погоду где-нибудь еще?', reply_markup=markup)

        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.END_STATE.value)

    else:
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.DETAIL_STATE.value)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt1 = telebot.types.KeyboardButton('Коротко')
        bt2 = telebot.types.KeyboardButton('Подробно')
        markup.add(bt1, bt2)
        bot.send_message(message.chat.id, 'Ошибка, выберите из списка ниже', reply_markup=markup)

@bot.message_handler(func=lambda message:
int(dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE))) == config.States.END_STATE.value)
def end(message):
    if message.text == 'Да':
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        markup.add(telebot.types.KeyboardButton('Геолокация', request_location=True))
        bot.send_message(message.chat.id, 'Отправь мне свою геолокацию или введи город!', reply_markup=markup)
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.LOCATION_STATE.value)
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Спасибо за использование этого бота!\nЧтобы начать напишите /start',
        reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add(telebot.types.KeyboardButton('Да'), telebot.types.KeyboardButton('Нет'))
        bot.send_message(message.chat.id, 'Не совсем понимаю, выберите кнопку ниже', reply_markup=markup)
        
if __name__ == '__main__':
    bot.infinity_polling()