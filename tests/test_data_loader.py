import unittest
from src.data_loader import load_data

class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        df = load_data('data/apple.csv')
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
