import sys
import os

# Add src directory to the Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

import pytest
import pandas as pd
from indicators import calculate_indicators

def test_calculate_indicators():
    data = pd.DataFrame({
        'Close': [100, 101, 102, 103, 104],
        'Date': pd.date_range(start='2023-01-01', periods=5)
    }).set_index('Date')
    
    data = calculate_indicators(data)
    
    assert 'SMA_50' in data.columns
    assert 'RSI' in data.columns
    assert 'MACD' in data.columns
