import pandas as pd
import streamlit as st
import yfinance as yf
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns

st.title('Stock Price Explorer')

ticket_symbol = st.text_input('Write the Stock Ticker Name', placeholder='AAPL')
if ticket_symbol=='':
    st.write('Please enter a stock ticker!')
else:
    start_date = st.date_input('Enter start date')
    end_date = st.date_input('Enter end date')
    data = yf.download(ticket_symbol, start_date, end_date)
    if data.empty:
        st.write('Invalid ticker or no data found!')
    else:
        data.columns = data.columns.droplevel(1)
        # simple moving average - average of 30, e.g. for day30 avg of day1 to day 30
        data['SMA_30'] = data['Close'].rolling(30).mean()
        st.dataframe(data)
        st.write('### Closing Price vs Time Chart')
        st.line_chart(data[['Close','SMA_30']])
        fig, ax = plt.subplots(figsize=(10, 4))
        st.write('### Trading Volume')
        ax.bar(data.index, data['Volume'], color='darkgray')
        ax.set_title('Trading Volume', fontsize=14)
        ax.set_ylabel('Shares Traded')
        st.pyplot(fig)

        data['Predicted_Target'] = data['Close'].shift(-1)
        data.dropna(inplace=True)

        X = data[['SMA_30']]
        y = data['Predicted_Target']
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        score = r2_score(y_test, y_pred)

        latest_data = data.iloc[[-1]][['SMA_30']]
        final_prediction = model.predict(latest_data)[0]

        st.write('### Correlation Heatmap')
        corr_matrix = data.corr()
        fig, ax = plt.subplots(figsize=(10, 8)) 
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
        ax.set_title('Stock Price Correlation Heatmap')
        st.pyplot(fig)

        st.header(f"Next Day Price Prediction")
        st.success(f"Predicted Closing Price: ${final_prediction:,.2f}")
        st.info(f"Model R² Score (Evaluation): {score:.4f}")