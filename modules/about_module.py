from telebot import types

def handle_about(message, bot):
    if message.text == 'О боте':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('На главную')
        markup.add(back)

        answer = 'Я бот, созданный <b>Матвеем и Лерой</b> для учебной практики БелГУ!\n'
        answer += 'Я умею общаться по кнопкам, которые тебе предложены, '
        answer += 'давай начнём наше знакомство😊'

        bot.send_message(message.chat.id, answer, reply_markup=markup, parse_mode='HTML')