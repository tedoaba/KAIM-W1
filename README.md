# KAIM Week 1 Challenges Task 2

## Stock Analysis with Sentiment and Correlation

## Overview

### Business Objective

Nova Financial Solutions aims to enhance its predictive analytics capabilities to significantly boost financial forecasting accuracy and operational efficiency. As a Data Analyst at Nova Financial Solutions, your primary task is to conduct a rigorous analysis of the financial news dataset. The focus of your analysis is two-fold:

1. **Sentiment Analysis**: Perform sentiment analysis on the 'headline' text to quantify the tone and sentiment expressed in financial news. Utilize natural language processing (NLP) techniques to derive sentiment scores and associate them with the respective 'Stock Symbol' to understand the emotional context surrounding stock-related news.

2. **Correlation Analysis**: Establish statistical correlations between the sentiment derived from news articles and the corresponding stock price movements. Track stock price changes around the date the article was published and analyze the impact of news sentiment on stock performance. Consider publication dates and times, if available.

Your recommendations should leverage insights from sentiment analysis to suggest investment strategies. These strategies should use the relationship between news sentiment and stock price fluctuations to predict future movements. The final report should offer clear, actionable insights based on your analysis and provide innovative strategies for utilizing news sentiment as a predictive tool for stock market trends.

### Dataset Overview

The **Financial News and Stock Price Integration Dataset (FNSPID)** is a comprehensive financial dataset designed to enhance stock market predictions by combining quantitative and qualitative data.

**Dataset Structure:**

- `headline`: Article release headline, the title of the news article, which often includes key financial actions like stocks hitting highs, price target changes, or company earnings.
- `url`: The direct link to the full news article.
- `publisher`: Author/creator of the article.
- `date`: The publication date and time, including timezone information (UTC-4 timezone).
- `stock`: Stock ticker symbol (unique series of letters assigned to a publicly traded company), for example, AAPL (Apple).

## Deliverables and Tasks

### 1. Quantitative Analysis Using PyNance and TA-Lib

#### Tasks:

1. **Load and Prepare the Data**:
   - Load stock price data into a pandas DataFrame. Ensure the data includes columns like Open, High, Low, Close, and Volume.

2. **Apply Analysis Indicators with TA-Lib**:
   - Use TA-Lib to calculate various technical indicators such as moving averages, RSI (Relative Strength Index), and MACD (Moving Average Convergence Divergence).

3. **Use PyNance for Financial Metrics**:
   - Implement additional financial metrics using PyNance.

4. **Visualize the Data**:
   - Create visualizations to better understand the data and the impact of different indicators on stock price.

### Minimum Essential To Do

1. **Prepare Your Data**:
   - Clean and preprocess the dataset for analysis.

2. **Calculate Basic Technical Indicators**:
   - Compute technical indicators like moving averages, RSI, and MACD.

3. **Visualize Data**:
   - Generate plots for stock price, moving averages, RSI, and MACD.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/tedoaba/KAIM-W1.git
   cd KAIM-W1
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   ```bash
   .\venv\Scripts\activate
   ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Contributing

1. **Fork the Repository**: Create your own fork of the repository on GitHub.
2. **Clone Your Fork**: Clone the fork to your local machine.
3. **Create a Branch**: Create a new branch for your feature or bug fix.
4. **Make Changes**: Implement your changes and test them.
5. **Submit a Pull Request**: Push your changes to your fork and submit a pull request to the main repository.
