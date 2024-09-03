import unittest
import pandas as pd
from src.data_merger import merge_data

class TestDataMerger(unittest.TestCase):

    def test_merge_data(self):
        news_data = {'date': ['2023-01-01', '2023-01-02'], 'headline': ['Good news', 'Bad news']}
        stock_data = {'date': ['2023-01-01', '2023-01-02'], 'Daily Return': [0.05, -0.02]}
        news_df = pd.DataFrame(news_data)
        stock_df = pd.DataFrame(stock_data)
        merged_df = merge_data(news_df, stock_df)
        self.assertEqual(merged_df.shape[0], 2)
        self.assertIn('Daily Return', merged_df.columns)

if __name__ == '__main__':
    unittest.main()
