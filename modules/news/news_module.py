from telebot import types

def handle_news(message, bot):
    if message.text == 'Новости':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('habr')
        button2 = types.KeyboardButton('vc')
        back = types.KeyboardButton('На главную')

        markup.add(button1, button2, back)
        answer = 'Выберите откуда вы хотите получить новости.'

        bot.send_message(message.chat.id, answer, reply_markup=markup)