from telebot import types
from modules.news.news_return import news_return

def news_num(message, bot, URL, tag):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Самая свежая новость')
    button2 = types.KeyboardButton('2 последние новости')
    button3 = types.KeyboardButton('3 последние новости')
    button4 = types.KeyboardButton('4 последние новости')
    button5 = types.KeyboardButton('5 последних новостей')
    button6 = types.KeyboardButton('6 последних новостей')
    markup.add(button1, button2, button3, button4, button5, button6)

    answer = 'Укажите количество новостей, которое вас интересует'
    bot.send_message(message.chat.id, answer, reply_markup=markup)

    bot.register_next_step_handler(message, news_return, bot, URL, tag)