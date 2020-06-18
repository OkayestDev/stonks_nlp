import os
from joblib import load, dump
from src.constants import model_filename

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_model():
    model = None
    with open(ROOT_DIR + "/" + model_filename, "rb") as file:
        model = load(file)
    return model
