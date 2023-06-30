from telebot import types
from modules.news.news_num import news_num

def handle_vc(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Популярное')
    button2 = types.KeyboardButton('Свежее')
    button3 = types.KeyboardButton('Компании')
    button4 = types.KeyboardButton('Вакансии')
    button5 = types.KeyboardButton('Мероприятия')
    markup.add(button1, button2, button3, button4, button5)

    answer = 'За какой промежуток вы бы хотели просмотреть новости на vc?'

    bot.send_message(message.chat.id, answer, reply_markup=markup)
    bot.register_next_step_handler(message, handle_vc_category, bot)

def handle_vc_category(message, bot):
    category = message.text

    url_category = {
        'Популярное': 'https://vc.ru/popular',
        'Свежее': 'https://vc.ru/new',
        'Компании': 'https://vc.ru/companies',
        'Вакансии': 'https://vc.ru/job',
        'Мероприятия': 'https://vc.ru/events',
    }

    URL = url_category.get(category)

    news_num(message, bot, URL, tag='vc')