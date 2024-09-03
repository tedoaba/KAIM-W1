from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.sentiment_analysis import analyze_sentiment
from src.data_merger import merge_data
from src.correlation_analysis import calculate_correlation
from src.visualization import plot_daily_returns, scatter_plot

def main():
    # Load data
    apple = load_data('data/apple.csv')
    news_df = load_data('data/news.csv')

    # Clean data
    apple = clean_data(apple, 'Date')
    news_df = clean_data(news_df, 'date')

    # Analyze sentiment
    news_df['sentiment'] = news_df['headline'].apply(analyze_sentiment)

    # Merge data
    stock_df = apple.copy()
    stock_df['Company'] = 'Apple'
    merged_df = merge_data(news_df, stock_df)

    # Calculate correlation
    daily_df = merged_df[['date', 'Daily Return', 'sentiment']]
    correlation = calculate_correlation(daily_df, 'sentiment', 'Daily Return')
    print(f'Pearson correlation coefficient: {correlation}')

    # Visualize
    plot_daily_returns(daily_df)
    scatter_plot(daily_df)

if __name__ == '__main__':
    main()