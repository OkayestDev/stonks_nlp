import os
import pickle
from constants import model_filename

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def save_model(model):
    file = open(ROOT_DIR + "/" + model_filename, "wb")
    pickle.dump(model, file)


def load_model():
    file = open(ROOT_DIR + "/" + model_filename, "rb")
    return pickle.load(file)
