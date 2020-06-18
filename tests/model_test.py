# Tests to ensure our model has been saved
# Load it and make some predictions
from unittest import TestCase
from src.model_loader import load_model


class Test(TestCase):
    def test_loading_model_and_making_a_prediction(self):
        model = load_model()
        example = [
            "SLB files for bankruptcy, expect stock fall",
            "Microsoft: Its free money",
        ]
        prediction = model.predict(example)
        self.assertEqual(prediction, [0, 2])
