from telebot import types

def start(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Новости')
    button2 = types.KeyboardButton('О боте')

    markup.add(button1, button2)

    answer = 'Привет, <b>{0.first_name}</b>!'.format(message.from_user)
    answer += ' Я обучен выполнять команды, которые доступны тебе по кнопкам, '
    answer += 'выбери, что тебя интересует😉'

    bot.send_message(message.chat.id, answer, reply_markup=markup, parse_mode='HTML')