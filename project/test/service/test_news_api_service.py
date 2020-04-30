import unittest

from project.service.news_api_service import NewsApiService
from project.service.article_listings import articles
class SentimentEngineTest(unittest.TestCase):

    def setUp(self):
        self.service = NewsApiService()


    def test_get_article_page(self):
        page = self.service.get_article_page("https://www.mirror.co.uk/news/world-news/victims-fury-brit-paedophile-makes-15256215")
        print(page)

    def test_get_article_content(self):
        page = self.service.get_article_page(
            "https://www.mirror.co.uk/news/world-news/victims-fury-brit-paedophile-makes-15256215")

        content = self.service.get_article_content(page)
        print(content)



