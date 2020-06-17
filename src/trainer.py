import pandas as pd
import string
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

df_tweet = pd.read_csv("data/tweets.csv", sep=",")

print(df_tweet.sentiment.value_counts())

classifier = LogisticRegression()
punctuations = string.punctuation
nlp = spacy.load("en_core_web_sm")
stop_words = spacy.lang.en.stop_words.STOP_WORDS
parser = English()

# Creating our tokenizer function
def spacy_tokenizer(sentence):
    # Creating our token object, which is used to create documents with linguistic annotations.
    my_tokens = parser(sentence)
    # Lemmatizing each token and converting each token into lowercase
    my_tokens = [
        word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_
        for word in my_tokens
    ]
    # Removing stop words
    my_tokens = [
        word
        for word in my_tokens
        if word not in stop_words and word not in punctuations
    ]
    # return preprocessed list of tokens
    return my_tokens


# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        # Cleaning Text
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}


# Basic function to clean the text
def clean_text(text):
    # Removing spaces and converting text into lowercase
    return text.strip().lower()


bow_vector = CountVectorizer(tokenizer=spacy_tokenizer, ngram_range=(1, 1))

tfidf_vector = TfidfVectorizer(tokenizer=spacy_tokenizer)

X = df_tweet["tweet"]  # the features we want to analyze
ylabels = df_tweet["sentiment"]  # the labels, or answers, we want to test against

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.3)

pipe = Pipeline(
    [("cleaner", predictors()), ("vectorizer", bow_vector), ("classifier", classifier)]
)

pipe.fit(X_train, y_train)

# Predicting with a test dataset
predicted = pipe.predict(X_test)

# Model Accuracy
print("Logistic Regression Accuracy:", metrics.accuracy_score(y_test, predicted))
print("Logistic Regression Precision:", metrics.precision_score(y_test, predicted))
print("Logistic Regression Recall:", metrics.recall_score(y_test, predicted))

# for (sample, pred) in zip(X_test, predicted):
# print(sample, "Prediction => ", pred)

# example = ["1", "30-Jul-18", "Heather Gray Fabric", "Hate it! Doesn't work"]
# print(pipe.predict(example))

# @todo save model
