import unittest
from src.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def test_analyze_sentiment_positive(self):
        text = "This is a great day for the stock market!"
        sentiment = analyze_sentiment(text)
        self.assertGreater(sentiment, 0)

    def test_analyze_sentiment_negative(self):
        text = "The stock market crashed badly."
        sentiment = analyze_sentiment(text)
        self.assertLess(sentiment, 0)

    def test_analyze_sentiment_neutral(self):
        text = "The stock market was stable today."
        sentiment = analyze_sentiment(text)
        self.assertEqual(sentiment, 0)

if __name__ == '__main__':
    unittest.main()
