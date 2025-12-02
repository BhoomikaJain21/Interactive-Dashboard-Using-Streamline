import pandas as pd
import streamlit as st
import yfinance as yf
from matplotlib import pyplot as plt
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
