from unittest import TestCase
import src.stonks_nlp as nlp


class Test(TestCase):
    tweet_one = "BP Faces $17.5B Q2 Hit, Expects Lower Oil Price $BP"
    tweet_two = "25 Stocks Moving in Monday's Pre-Market Session $ISEE $VTVT $BBI $FLDM $WUBA $HTZ $PYX $CVGI $PCG $BTU"
    tweet_three = """
        The volatility index $VIX increased by more than 50% this week. 
        Historically, this has been a great sign for investors: The S&P 500 $SPY has gone higher the following week 71% of the time.

        Next week should be a very good week for stocks.

        $QQQ $IWM $XLF $JPM $WFC $FB
    """

    def test_tweet_one_returns_0(self):
        result = nlp.get_sentiment_of_tweet(self.tweet_one)
        self.assertEqual(0, result)

    def test_tweet_two_returns_1(self):
        result = nlp.get_sentiment_of_tweet(self.tweet_two)
        self.assertEqual(1, result)

    def test_tweet_three_returns_2(self):
        result = nlp.get_sentiment_of_tweet(self.tweet_three)
        self.assertEqual(2, result)