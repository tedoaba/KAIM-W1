# KAIM Week 1 Challenges Task 3

## Project Overview

### Business Objective

Nova Financial Solutions aims to significantly boost its financial forecasting accuracy and operational efficiency through advanced data analysis. As a Data Analyst at Nova Financial Solutions, your primary task is to conduct a rigorous analysis of a financial news dataset, focusing on two key areas:

1. **Sentiment Analysis**: Perform sentiment analysis on the ‘headline’ text to quantify the tone and sentiment expressed in financial news. The goal is to derive sentiment scores associated with the respective 'Stock Symbol' to understand the emotional context surrounding stock-related news.

2. **Correlation Analysis**: Establish statistical correlations between the sentiment derived from news articles and the corresponding stock price movements. This involves tracking stock price changes around the publication date of the article and analyzing the impact of news sentiment on stock performance. Your analysis should provide insights into the relationship between news sentiment and stock price fluctuations to predict future movements.

### Dataset Overview

The dataset used in this project, referred to as the Financial News and Stock Price Integration Dataset (FNSPID), is a comprehensive dataset designed to enhance stock market predictions by combining quantitative and qualitative data.

#### Dataset Structure:

- **headline**: The title of the news article, which often includes key financial actions like stocks hitting highs, price target changes, or company earnings.
- **url**: The direct link to the full news article.
- **publisher**: The author or creator of the article.
- **date**: The publication date and time, including timezone information (UTC-4 timezone).
- **stock**: Stock ticker symbol (a unique series of letters assigned to a publicly traded company).
- **Stock dataset columns**: ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Company'].

### Analysis Overview

#### Tasks

1. **Date Alignment**: Ensure that both datasets (news and stock prices) are aligned by dates, which might involve normalizing timestamps.
2. **Sentiment Analysis**: Conduct sentiment analysis on news headlines to quantify the tone of each article (positive, negative, neutral) using Python libraries like NLTK and TextBlob.
3. **Daily Stock Returns Calculation**: Compute the percentage change in daily closing prices to represent stock movements.
4. **Correlation Analysis**: Use statistical methods to test the correlation between daily news sentiment scores and stock returns.

#### Minimum Essential To-Do

- **Data Preparation**:
  - Normalize dates to align both news and stock datasets, ensuring each news item matches the corresponding stock trading day.
  - Perform sentiment analysis to assign sentiment scores to headlines.

- **Stock Movements Calculation**:
  - Compute daily returns by calculating daily percentage changes in stock prices to represent movements.

- **Correlation Analysis**:
  - Aggregate sentiments by computing average daily sentiment scores if multiple articles appear on the same day.
  - Calculate the Pearson correlation coefficient between average daily sentiment scores and stock daily returns.

## Tests

Each module is accompanied by a corresponding test file in the `tests/` directory:

## CI/CD Integration

Continuous Integration/Continuous Deployment (CI/CD) is set up using GitHub Actions. The CI pipeline includes the following steps:

1. **Install Dependencies**: Install all the necessary dependencies listed in `requirements.txt`.
2. **Run Tests**: Execute all the test cases to ensure that each module is functioning correctly.
3. **Build and Deploy**: Build and deploy the project, ensuring that the latest changes are always reflected in the production environment.

The GitHub Actions workflow file (`ci.yml`) is located in the `.github/workflows/` directory.

## Requirements

To install the necessary packages, run:

```bash
pip install -r requirements.txt
```

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/tedoaba/KAIM-W1.git
```

2. **Navigate to the project directory**

```bash
cd KAIM-w1
```

3. **Checkout to `task-3` branch**

```bash
git checkout task-3
```

4. **Run the analysis**

```bash
cd scripts
python main.py
```

5. **Run tests**

```bash
python -m unittest discover tests
```

## Conclusion

This project provides a framework for analyzing the correlation between financial news sentiment and stock market movements. By leveraging natural language processing techniques and statistical analysis, it offers insights that can be utilized for predictive financial modeling and strategic investment decisions.
