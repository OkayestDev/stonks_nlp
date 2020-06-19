from src.model_loader import load_model

model = load_model()

def get_sentiment_of_tweet(tweet):
    result = model.predict(tweet)
    return result