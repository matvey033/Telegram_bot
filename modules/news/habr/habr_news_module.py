from telebot import types
from modules.news.news_num import news_num

def handle_habr(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Все потоки')
    button2 = types.KeyboardButton('Разработка')
    button3 = types.KeyboardButton('Научпоп')
    button4 = types.KeyboardButton('Дизайн')
    button5 = types.KeyboardButton('Менеджмент')
    button6 = types.KeyboardButton('Маркетинг')
    button7 = types.KeyboardButton('Администрирование')
    markup.add(button1, button2, button3, button4, button5, button6, button7)

    answer = 'Какая категория вас интересует?'
    bot.send_message(message.chat.id, answer, reply_markup=markup)

    bot.register_next_step_handler(message, handle_habr_category, bot)

def handle_habr_category(message, bot):
    category = message.text

    url_category = {
        'Все потоки': 'https://habr.com/ru/all/',
        'Разработка': 'https://habr.com/ru/flows/develop/',
        'Администрирование': 'https://habr.com/ru/flows/admin/',
        'Дизайн': 'https://habr.com/ru/flows/design/',
        'Менеджмент': 'https://habr.com/ru/flows/management/',
        'Маркетинг': 'https://habr.com/ru/flows/marketing/',
        'Научпоп': 'https://habr.com/ru/flows/popsci/'
    }

    URL = url_category.get(category)
    
    news_num(message, bot, URL, tag='habr')