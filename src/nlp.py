import spacy
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
import string

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

nlp = spacy.load("en_core_web_sm")
parser = English()
punctuations = string.punctuation
stopwords = list(STOP_WORDS)


def spacy_tokenizer(tweet):
    my_tokens = parser(tweet)
    my_tokens = [
        word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_
        for word in my_tokens
    ]
    my_tokens = [
        word for word in my_tokens if word not in stopwords and word not in punctuations
    ]
    return my_tokens


def get_sentiment_of_tweet(tweet):
    doc = nlp(tweet)
    my_tokens = spacy_tokenizer(tweet)

    # # Find named entities, phrases and concepts
    # for token in doc:
    #     print(token)

    return {"is_buy": False, "stocks": ["BP"]}
