from modules.news.habr.parser_habr import scrape_habr
from modules.news.vс.parser_vc import scrape_vc
from modules.end_module import end

def news_return(message, bot, URL, tag):
    num = message.text

    count_news = {
        'Самая свежая новость': 1,
        '2 последние новости': 2,
        '3 последние новости': 3,
        '4 последние новости': 4,
        '5 последних новостей': 5,
        '6 последних новостей': 6,
    }
    num_news = count_news.get(num)

    if tag == 'vc': news_list = scrape_vc(URL, num_news)
    if tag == 'habr': news_list = scrape_habr(URL, num_news)

    for news in news_list:
        title = news['title']
        description = news['description']
        URL = news['url']

        news = f'{title}{description}{URL}'
        bot.send_message(message.chat.id, news, parse_mode='HTML')
    end(message, bot)