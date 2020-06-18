from src.model_loader import load_model

model = load_model()

def get_sentiment_of_tweet(tweet):
    tweet = [tweet]
    result = model.pipe.predict(tweet)
    return result[0]