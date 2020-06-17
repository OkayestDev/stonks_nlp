import logging
import json

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def determine_tweet_sentiment(tweet):
    return True


def handler(event, context):
    LOGGER.info(event)
    tweet = event['tweet']
    tweet_sentiment = determine_tweet_sentiment(tweet)
    return {
        "tweet_sentiment": tweet_sentiment,
        "tweet": tweet,
        "message": "Hello pytest!"
    }
