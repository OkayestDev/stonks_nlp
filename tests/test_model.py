# Tests to ensure our model has been saved
# Load it and make some predictions
import src
from unittest import TestCase
from src.model_loader import load_model


class Test(TestCase):
    # this test will fail until we have sufficient data in in tweets.csv
    def test_loading_model_and_making_a_prediction(self):
        model = load_model()
        example = [
            "SLB files for bankruptcy, expect stock fall",
            "Microsoft: Its free money",
        ]
        prediction = model.pipe.predict(example)
        print(prediction)
        self.assertEqual(prediction[0], 0)
        self.assertEqual(prediction[1], 2)
