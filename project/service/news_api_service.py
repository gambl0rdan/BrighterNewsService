import requests
from bs4 import BeautifulSoup

class NewsApiService(object):
    # Classes
    # body-content or main-content //Independant
    # article-body // Mirror
    # story-body or story-body__inner//BBC news

    def get_article_page(self, url):
        return requests.get(url)

    def get_article_content(self, page):
        contents = ''
        ID_KEYS = ['main', 'content', 'main-content', 'all', 'article-body']

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            resp = soup.find_all(class_='article-body')

            if resp:

                paragraphs = resp[0].find_all('p')
                for p in paragraphs:
                    contents = contents + p.text
            else:
                for key in ID_KEYS:
                    resp = soup.find(id=key)
                    if resp:
                        break

                if resp:
                    paragraphs = resp.find_all('p')

                    if not paragraphs:
                        paragraphs = soup.findAll('p')

                    for p in paragraphs:
                        contents = contents + p.text

        return contents

    def get_articles_from_everything(self, response):
        results = []
        contents = ''
        if response.status_code == 200:
            urlsDescs = [(res['url'], res['content']) for res in response.json()['articles']]
            return urlsDescs
        return []
