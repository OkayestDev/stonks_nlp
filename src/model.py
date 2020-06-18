import spacy
import string
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Self contained sklearn model. This class is what is saved in stonks_model
class Model:
    def __init__(self, X, ylabels):
        self.classifier = LogisticRegression()
        self.punctuations = string.punctuation
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = spacy.lang.en.stop_words.STOP_WORDS
        self.parser = English()
        self.bow_vector = CountVectorizer(
            tokenizer=self.spacy_tokenizer, ngram_range=(1, 1)
        )
        self.tfidf_vector = TfidfVectorizer(tokenizer=self.spacy_tokenizer)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, ylabels, test_size=0.3
        )

        self.pipe = Pipeline(
            [
                ("cleaner", self.predictors()),
                ("vectorizer", self.bow_vector),
                ("classifier", self.classifier),
            ]
        )

        self.pipe.fit(self.X_train, self.y_train)

    # Creating our tokenizer function
    def spacy_tokenizer(self, sentence):
        # Creating our token object, which is used to create documents with linguistic annotations.
        my_tokens = self.parser(sentence)
        # Lemmatizing each token and converting each token into lowercase
        my_tokens = [
            word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_
            for word in my_tokens
        ]
        # Removing stop words
        my_tokens = [
            word
            for word in my_tokens
            if word not in self.stop_words and word not in self.punctuations
        ]
        # return preprocessed list of tokens
        return my_tokens

    class predictors(TransformerMixin):
        def transform(self, X, **transform_params):
            # Cleaning Text
            return [self.clean_text(text) for text in X]

        def fit(self, X, y=None, **fit_params):
            return self

        def get_params(self, deep=True):
            return {}

        def clean_text(self, text):
            return text.strip().lower()

