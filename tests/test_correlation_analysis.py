import unittest
import pandas as pd
from src.correlation_analysis import calculate_correlation

class TestCorrelationAnalysis(unittest.TestCase):

    def test_calculate_correlation(self):
        data = {'sentiment': [0.1, 0.2, 0.3, 0.4], 'Daily Return': [0.01, 0.02, 0.03, 0.04]}
        df = pd.DataFrame(data)
        correlation = calculate_correlation(df, 'sentiment', 'Daily Return')
        self.assertAlmostEqual(correlation, 1.0, places=2)

if __name__ == '__main__':
    unittest.main()
