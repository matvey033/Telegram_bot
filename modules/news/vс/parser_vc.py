import requests
from bs4 import BeautifulSoup

def scrape_vc(URL, num_news):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    posts = soup.find_all('div', class_='feed__item l-island-round')
    news_list = []

    for post in posts[:num_news]:
        try: title = '<b>Заголовок:</b> <i>' + post.find('div', class_='content-title').text.strip() + '</i>' + '\n\n'
        except Exception: title = ''

        try: description = '<b>Описание:</b> <i>' + post.find('div', class_='content-container').find('p').text.strip() + '</i>' + '\n\n'
        except Exception: description = ''

        try: url = '<b>Ссылка на статью:</b> ' + post.find('a', class_='content-link')['href'].strip() + '\n\n'
        except Exception: url = ''
        
        news_list.append({'title': title, 'description': description, 'url': url})
    return news_list