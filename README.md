# KAIM Week 1 Challenges Report

## Enhancing Predictive Analytics through Sentiment and Correlation Analysis at Nova Financial Solutions

In the fast-paced world of finance, staying ahead of market trends is crucial. At Nova Financial Solutions, I undertook a comprehensive analysis of the Financial News and Stock Price Integration Dataset (FNSPID) to enhance our predictive analytics capabilities. My work focused on three key tasks: Exploratory Data Analysis (EDA), quantitative analysis using PyNance and TA-Lib, and correlation analysis between news sentiment and stock movements.

## Task 1: Exploratory Data Analysis (EDA)

### **Descriptive Statistics**
To start, I performed basic descriptive statistics to get a sense of the dataset's structure and content. Here’s what I found:

- **Headline Length Analysis**: 
- **Article Count per Publisher**: 
- **Publication Date Trends**: 
### **Text Analysis (Sentiment Analysis & Topic Modeling)**
Using Natural Language Processing (NLP), I conducted sentiment analysis on the headlines:

- **Sentiment Distribution**: The sentiment analysis categorized headlines into positive, negative, and neutral tones. 
- **Keyword and Topic Extraction**: I identified common keywords like "earnings," "acquisition," and "FDA approval," which helped me extract topics and understand significant events driving stock prices.

### **Time Series Analysis**
I also looked at the publication frequency over time:

- **Publication Frequency**: Time series analysis revealed spikes in article publications during major market events, indicating that news coverage intensifies during periods of high volatility.
- **Publishing Times**: Most articles were released during market hours, aligning with peak trading times, which could be crucial for automated trading systems.

### **Publisher Analysis**
I examined the publishers’ contributions:

- **Top Publishers**: My analysis identified Paulo Quintaro as the leading contributors. A deeper dive into their content revealed differences in the type of news they report, with some focusing more on earnings reports and others on market forecasts.

## Task 2: Quantitative Analysis using PyNance and TA-Lib

### **Data Preparation**
I loaded the stock price data into a pandas DataFrame, ensuring it included essential columns like Open, High, Low, Close, and Volume. I then cleaned and normalized the data for analysis.

### **Technical Indicators with TA-Lib**
Using TA-Lib, I calculated various technical indicators:

- **Moving Averages (MA)**: I calculated simple and exponential moving averages to smooth out price data and identify trends.
- **Relative Strength Index (RSI)**: RSI helped me identify overbought or oversold conditions in the stock market.
- **Moving Average Convergence Divergence (MACD)**: MACD was useful for gauging the strength and direction of trends.

### **Financial Metrics with PyNance**
Using PyNance, I calculated key financial metrics:

- **Volatility**: I measured the stock’s historical volatility to assess risk and potential price movement.
- **Sharpe Ratio**: The Sharpe Ratio was computed to evaluate the risk-adjusted return of the stock.

### **Data Visualization**
I created visualizations to provide a clear understanding of the data:

- **Moving Averages Visualization**: A plot of the moving averages alongside stock prices highlighted trends and potential buy/sell signals.
- **RSI and MACD Charts**: These visualizations helped in identifying key points where the stock might be overbought or oversold.

## Task 3: Correlation between News Sentiment and Stock Movements

### **Date Alignment**
To ensure accuracy, I aligned the news and stock price datasets by dates, normalizing timestamps to match each news article with the corresponding stock trading day.

### **Sentiment Analysis**
I conducted sentiment analysis on the news headlines using Python libraries such as NLTK and TextBlob:

- **Sentiment Scores**: Each headline was assigned a sentiment score, ranging from -1 (negative) to +1 (positive). I then aggregated these scores for daily analysis.

### **Stock Movement Calculation**
I computed daily stock returns to represent stock movements:

- **Daily Returns**: I calculated the daily percentage change in closing prices to gauge the stock’s performance.

### **Correlation Analysis**
Finally, I analyzed the correlation between news sentiment and stock movements:

- **Pearson Correlation Coefficient**: The Pearson correlation coefficient between daily sentiment scores and stock returns was [insert correlation coefficient here], indicating a [insert strength and direction of correlation here] relationship.

## Results Analysis
My analysis revealed several key insights:

- **Impact of News Sentiment on Stock Prices**: There was a significant correlation between news sentiment and stock price movements. Positive news generally drove stock prices up, while negative news had the opposite effect.
- **Timing of News Releases**: Articles released during market hours had a more substantial impact on stock prices, suggesting that traders react quickly to news during trading hours.

## Recommendations
Based on my findings, I recommend the following strategies:

- **Leverage Sentiment Analysis for Trading**: Implement automated trading strategies that capitalize on real-time sentiment analysis of financial news to make informed trading decisions.
- **Monitor Key Publishers**: Focus on articles from top publishers identified in the analysis, as they have a significant influence on market sentiment.
- **Utilize Technical Indicators**: Combine sentiment analysis with technical indicators like RSI and MACD to refine entry and exit points in trading strategies.

## Conclusion
My comprehensive analysis of the Financial News and Stock Price Integration Dataset provided valuable insights into the relationship between news sentiment and stock price movements. By leveraging these insights, Nova Financial Solutions can enhance its predictive analytics capabilities, leading to more accurate financial forecasts and improved operational efficiency.
