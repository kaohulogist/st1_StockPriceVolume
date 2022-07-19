import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
 
 Show are the **closing price** and the **volume** of stocks!
 
""")

tickerSymbol = ["GOOGL", "TSLA","UPST","AAPL"]
for symbol in tickerSymbol:
    tickerData = yf.Ticker(symbol)
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-7-18')
    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)

    st.write("""
    ## Volume 
    """)
    st.bar_chart(tickerDf.Volume)
   