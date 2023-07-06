from telebot import types

def handle_unknown(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Новости')
    button2 = types.KeyboardButton('О боте')

    markup.add(button1, button2)

    answer = '<b>К сожалению</b>😢, меня обучили только общению по предложенным кнопкам, '
    answer += 'поэтому вам стоит выбирать ответы из предложенных вариантов, чтобы я мог вас понимать. '
    answer += 'Если вы ещё не начади взаимодействовать со мной, то просто введите <i>/start</i>.'
    bot.send_message(message.chat.id, answer, reply_markup=markup, parse_mode='HTML')