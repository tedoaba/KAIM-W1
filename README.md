# Financial News Sentiment and Stock Price Correlation Analysis

## Project Overview

Nova Financial Solutions aims to enhance its predictive analytics capabilities to significantly boost financial forecasting accuracy and operational efficiency. This project focuses on analyzing a financial news dataset to explore the relationship between the sentiment of news headlines and stock price movements.

As part of this project, we conducted a rigorous analysis of the Financial News and Stock Price Integration Dataset (FNSPID), focusing on sentiment analysis and correlation analysis. Our goal is to derive actionable insights that can inform investment strategies and predict future stock market trends based on news sentiment.

## Table of Contents

- [Financial News Sentiment and Stock Price Correlation Analysis](#financial-news-sentiment-and-stock-price-correlation-analysis)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Dataset Overview](#dataset-overview)
  - [Analysis Objectives](#analysis-objectives)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Results](#results)
  - [Recommendations](#recommendations)
  - [Contributing](#contributing)

## Dataset Overview

**Financial News and Stock Price Integration Dataset (FNSPID):**

- **headline:** Article release headline, often including key financial actions like stocks hitting highs, price target changes, or company earnings.
- **url:** The direct link to the full news article.
- **publisher:** Author/creator of the article.
- **date:** The publication date and time, including timezone information (UTC-4).
- **stock:** Stock ticker symbol (e.g., AAPL for Apple).

## Analysis Objectives

1. **Sentiment Analysis:**
   - Perform sentiment analysis on the headlines to quantify the tone (positive, negative, neutral) expressed in financial news.
   - Associate sentiment scores with the respective stock symbols to understand the emotional context surrounding stock-related news.

2. **Correlation Analysis:**
   - Establish statistical correlations between the sentiment derived from news articles and the corresponding stock price movements.
   - Analyze the impact of news sentiment on stock performance around the publication date.

3. **Exploratory Data Analysis (EDA):**
   - Descriptive statistics, text analysis, time series analysis, and publisher analysis to understand the dataset better and uncover patterns.

## Project Structure

- **`notebooks/`**: Jupyter notebooks used for data exploration, analysis, and visualization.
- **`src/`**: Python scripts and modules for data processing, sentiment analysis, and correlation analysis.
- **`scripts/`**: Contains all scripts of the project.
- **`README.md`**: Project overview and documentation (this file).

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/tedoaba/kaim_w1.git
   cd kaim_w1
   ```

2. Create a virtual environment and activate it:

   ```bash

   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash

   pip install -r requirements.txt
   ```

## Usage

1. **Data Analysis:**
   - The notebooks in the `notebooks/` directory provide step-by-step analysis of the dataset.
   - Use `src/` for running sentiment and correlation analysis scripts.

2. **Git Workflow:**
   - Create a new branch for analysis tasks:
  
     ```bash
     git checkout -b task-1
     ```

   - Commit your work with descriptive messages:

     ```bash
     git commit -m "Descriptive message of the task"
     ```

   - Push changes to the repository:

     ```bash
     git push origin task-1
     ```

## Results

The analysis provided the following key insights:

- [Summary of Sentiment Analysis Results]
- [Summary of Correlation Analysis Results]
- [Key Findings from EDA]

## Recommendations

Based on the analysis, ...

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or additional analysis.

