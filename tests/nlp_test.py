from unittest import TestCase
import src.nlp as nlp

class Test(TestCase):
    tweet_one = "BP Faces $17.5B Q2 Hit, Expects Lower Oil Price $BP"
    tweet_two = "25 Stocks Moving in Monday's Pre-Market Session $ISEE $VTVT $BBI $FLDM $WUBA $HTZ $PYX $CVGI $PCG $BTU"
    tweet_three = """
        The volatility index $VIX increased by more than 50% this week. 
        Historically, this has been a great sign for investors: The S&P 500 $SPY has gone higher the following week 71% of the time.

        Next week should be a very good week for stocks.

        $QQQ $IWM $XLF $JPM $WFC $FB
    """

    def test_tweet_one_returns_no_by_for_BP_stock(self):
        result = nlp.get_sentiment_of_tweet(self.tweet_one)
        self.assertEqual(result["is_buy"], False)
        self.assertEqual(result["stocks"], ["BP"])
