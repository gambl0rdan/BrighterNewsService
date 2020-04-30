import unittest

from project.service.sentiment_engine import SentimentEngine
from project.service.article_listings import articles

class SentimentEngineTest(unittest.TestCase):

    def setUp(self):
        self.engine = SentimentEngine()

    def testKnownSadHeadline(self):

        input = "British paedophile Christopher Trinnaman grins as he stands surrounded by unsuspecting kids in his new home of Vietnam.\r\nThe twisted trombone player, 41, moved to the south-east Asian country after he was released from jail in 2015 and signed up with a top or… "
        actRes = self.engine.get_scores_headline(input)
        self.assertLessEqual(actRes, 0.5)

    def testKnownSadArticle(self):
        input = articles['bad-man']
        actRes = self.engine.get_scores_headline(input)
        self.assertLessEqual(actRes, 0.)