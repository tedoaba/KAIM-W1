import pandas as pd

def calculate_correlation(df, col1, col2):
    return df[[col1, col2]].corr().iloc[0, 1]
