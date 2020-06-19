# Tests to ensure our model has been saved
# Load it and make some predictions
import src
from unittest import TestCase
from src.model_loader import load_model

model = load_model()

class Test(TestCase):
    # this test will fail until we have sufficient data in in tweets.csv
    def test_loading_model_and_making_a_prediction(self):
        example = [
            "SLB files for bankruptcy, expect stock fall",
            "Microsoft: Its free money",
        ]
        prediction = model.pipe.predict(example)
        self.assertEqual(prediction[0], 0)
        self.assertEqual(prediction[1], 1)

    def test_predict_returns_prediction(self):
        tweet = """
            The volatility index $VIX increased by more than 50% this week. 
            Historically, this has been a great sign for investors: The S&P 500 $SPY has gone higher the following week 71% of the time.

            Next week should be a very good week for stocks.

            $QQQ $IWM $XLF $JPM $WFC $FB
        """
        prediction = model.predict(tweet)
        self.assertEqual(1, prediction)
