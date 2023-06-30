import telebot
import config

from modules.start_module import start
from modules.about_module import handle_about
from modules.unknown_module import handle_unknown

from modules.news.news_module import handle_news

from modules.news.habr.habr_news_module import handle_habr
from modules.news.vс.vс_news_module import handle_vc


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    start(message, bot)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.chat.type == 'private':
        command_handlers = {
            'Новости': handle_news,
            'habr': handle_habr,
            'vc': handle_vc,
            'О боте': handle_about,
            'На главную': start,
        }

        command = message.text
        handler = command_handlers.get(command, handle_unknown)
        handler(message, bot)

bot.polling(none_stop=True)