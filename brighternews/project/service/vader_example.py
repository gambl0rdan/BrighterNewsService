import nltk

from article_listings import headlines
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

for name, passage in headlines:
    scores = sia.polarity_scores(passage)
    print (name, scores)
