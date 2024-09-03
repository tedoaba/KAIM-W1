import sys
import os

# Add src directory to the Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

import os
import pandas as pd
from visualization import plot_moving_averages, plot_rsi, plot_macd

def test_plot_moving_averages():
    data = pd.DataFrame({
        'Close': [100, 101, 102, 103, 104],
        'SMA_50': [None, None, None, None, 102],
        'SMA_200': [None, None, None, None, None],
        'Date': pd.date_range(start='2023-01-01', periods=5)
    }).set_index('Date')
    
    plot_moving_averages(data, 'test_moving_averages.png')
    assert os.path.isfile('test_moving_averages.png')
