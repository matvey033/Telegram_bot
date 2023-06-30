from telebot import types

def end(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Новости')
    button2 = types.KeyboardButton('О боте')

    markup.add(button1, button2)

    answer = '<b>{0.first_name}</b>,'.format(message.from_user)
    answer += ' если ты хочешь узнать что-то ещё, то нажми на нужные кнопки.\n\n'
    answer += 'Также более подробно с новостями ты можешь ознакомиться на '
    answer += '<i>habr.com</i> и на <i>vc.ru</i>'

    bot.send_message(message.chat.id, answer, reply_markup=markup, parse_mode='HTML')