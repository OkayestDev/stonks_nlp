import pandas as pd
import os
from sklearn import metrics
from src.model import Model
from joblib import load, dump
from src.constants import model_filename

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
df_tweet = pd.read_csv(ROOT_DIR + "/data/tweets.csv", sep=",")

X = df_tweet["tweet"]  # the features we want to analyze
ylabels = df_tweet["sentiment"]  # the labels, or answers, we want to test against

print(df_tweet.sentiment.value_counts())

# Used to create a new model from our base tweets data, tweets.csv
# @todo add a conditional to prevent accidentally overwriting model
model = Model(X, ylabels)

# Predicting with a test dataset
predicted = model.pipe.predict(model.X_test)

# Model Accuracy
print("Logistic Regression Accuracy:", metrics.accuracy_score(model.y_test, predicted))
print(
    "Logistic Regression Precision:",
    metrics.precision_score(model.y_test, predicted, average="micro"),
)
print(
    "Logistic Regression Recall:",
    metrics.recall_score(model.y_test, predicted, average="micro"),
)

example = [
    "SLB files for bankruptcy, expect stock fall",
    "Microsoft: Its free money",
]
print(model.pipe.predict(example))

# saving the model
file = open(ROOT_DIR + "/" + model_filename, "wb")
dump(model, file)
file.close()
