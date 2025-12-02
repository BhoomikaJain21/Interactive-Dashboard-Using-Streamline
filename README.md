# Interactive Stock Price Explorer (Streamlit App)

## 🌟 Project Overview

This is an interactive web application built in Python using **Streamlit** to provide a simple, real-time tool for historical stock price analysis. The application allows users to query any stock ticker, define a date range, and instantly view closing price trends and trading volumes.

The primary objective was to gain practical proficiency in integrating the **yfinance** library for financial data fetching and using **Pandas** and **Matplotlib** for data processing and visualization within a deployable **Streamlit** interface.

## 💡 Key Features

* **Custom Data Fetching:** Utilizes the `yfinance` library to fetch daily historical data for any valid ticker symbol (e.g., AAPL, GOOGL).
* **Technical Analysis:** Calculates and displays the **30-Day Simple Moving Average (SMA_30)**, overlaid on the closing price chart for trend analysis.
* **Visualization:** Displays two main charts:
    1.  Closing Price vs. Time (with SMA_30)
    2.  Trading Volume (Bar Chart)
* **Interactive Inputs:** Uses Streamlit widgets for ticker symbol, start date, and end date inputs.

## ⚙️ Technologies Used

* **Python:** Core programming language.
* **Streamlit:** For building the interactive web interface.
* **Pandas:** For data loading, manipulation, calculating the SMA (using `.rolling().mean()`), and data frame preparation.
* **Matplotlib / pyplot:** For generating the trading volume bar chart.
* **yfinance:** For reliable historical stock data retrieval.

## 🚀 Getting Started

**Prerequisites:**

* Python 3.x

**Installation and Setup:**

1.  **Install Dependencies:**
    ```bash
    pip install streamlit pandas matplotlib yfinance seaborn
    ```
2.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```
