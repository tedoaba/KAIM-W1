import sys
import os

# Add src directory to the Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

import pytest
import pandas as pd
from data_preprocessing import load_data

def test_load_data():
    data = load_data('/path/to/test_data.csv')
    assert isinstance(data, pd.DataFrame)
    assert 'Date' in data.columns
    assert data.index.name == 'Date'
