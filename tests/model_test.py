# Tests to ensure our model has been saved
# Load it and make some predictions
from unittest import TestCase
from src.constants import model_filename
import pickle
import os


class Test(TestCase):
    def test_loading_model_and_making_a_prediction(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        path_to_model = ROOT_DIR + "/../src/" + model_filename
        model = pickle.load(open(path_to_model, "rb"))
        example = [
            "SLB files for bankruptcy, expect stock fall",
            "Microsoft: Its free money",
        ]
        prediction = model.predict(example)
        self.assertEqual(prediction, [0, 2])
