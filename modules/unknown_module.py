def handle_unknown(message, bot):
    answer = 'К сожалению😢, меня обучили только общению по предложенным кнопкам, '
    answer += 'если хотите начать взаимодействовать со мной, то введите /start.'
    bot.send_message(message.chat.id, answer)