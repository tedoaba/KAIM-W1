import unittest
import pandas as pd
from src.visualization import plot_daily_returns, scatter_plot

class TestVisualization(unittest.TestCase):

    def test_plot_daily_returns(self):
        data = {'date': ['2023-01-01', '2023-01-02'], 'Daily Return': [0.05, -0.02]}
        daily_df = pd.DataFrame(data)
        try:
            plot_daily_returns(daily_df)
        except Exception as e:
            self.fail(f"plot_daily_returns raised {type(e).__name__} unexpectedly!")

    def test_scatter_plot(self):
        data = {'Average Sentiment': [0.1, 0.2], 'Daily Return': [0.05, -0.02]}
        daily_df = pd.DataFrame(data)
        try:
            scatter_plot(daily_df)
        except Exception as e:
            self.fail(f"scatter_plot raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()
