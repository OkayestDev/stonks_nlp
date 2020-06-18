import sys
from src.stonks_nlp import get_sentiment_of_tweet

# sys[0] is filename
tweet = sys.argv[1]
result = get_sentiment_of_tweet(tweet)
print(result)