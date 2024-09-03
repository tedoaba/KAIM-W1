import unittest
import pandas as pd
from src.data_cleaner import clean_data

class TestDataCleaner(unittest.TestCase):

    def test_clean_data(self):
        data = {'Date': ['2023-01-01', '2023-01-02', None]}
        df = pd.DataFrame(data)
        cleaned_df = clean_data(df, 'Date')
        self.assertFalse(cleaned_df.empty)
        self.assertEqual(cleaned_df.shape[0], 2)
        self.assertFalse(cleaned_df['Date'].isnull().any())

if __name__ == '__main__':
    unittest.main()
