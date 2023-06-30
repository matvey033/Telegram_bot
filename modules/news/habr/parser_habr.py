import requests
from bs4 import BeautifulSoup

def scrape_habr(URL, num_news):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    posts = soup.find_all('article', class_='tm-articles-list__item', id=True)
    news_list = []

    for post in posts[:num_news]:
        try: title = '<b>Заголовок:</b> <i>' + post.find('h2', class_='tm-title tm-title_h2').text.strip() + '</i>' + '\n\n'
        except Exception: title = ''

        try: author = '<b>Автор:</b> <i>' + soup.find("a", class_="tm-user-info__username").text.strip() + '</i>\n'
        except Exception: author = ''
        try: reading_time = '<b>Время чтения:</b> <i>' + soup.find("span", class_="tm-article-reading-time__label").text.strip() + '</i>\n'
        except Exception: reading_time = ''
        try: views = '<b>Количество просмотров:</b> <i>' + soup.find("span", class_="tm-icon-counter__value").text.strip() + '</i>'
        except Exception: views = ''

        try: description = '<u>Информация о статье:\n</u>' + author + reading_time + views + '\n\n'
        except Exception: description = ''

        try: url = '<b>Ссылка на статью:</b> ' + 'https://habr.com' + post.find('a', class_='tm-title__link', href=True)['href'].strip() + '\n\n'
        except Exception: url = ''

        news_list.append({'title': title, 'description': description, 'url': url})

    return news_list
