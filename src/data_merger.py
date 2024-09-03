import pandas as pd

def merge_data(news_df, stock_df, on='date'):
    merged_df = pd.merge(news_df, stock_df, on=on)
    return merged_df
