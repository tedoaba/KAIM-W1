import pandas as pd

def clean_data(df, date_column):
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce').dt.tz_localize(None)
    df.dropna(inplace=True)
    return df
