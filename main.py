import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd


def stock_ticker(name):
	company = yf.Ticker(name) 
	return company

st.title("StockWizzard")

st.subheader('A responsive, stock ticker data science and data analytics app')

st.subheader('Provides data on multiple companies listed in the NASDAQ marketplace', divider='rainbow')




company1 = stock_ticker("TSLA")
company2 = stock_ticker("AAPL")
company3 = stock_ticker("AMZN")
company4 = stock_ticker("V")
company5 = stock_ticker("DOW")
company6 = stock_ticker("BRK-A")
company7 = stock_ticker("MA")

tesla = yf.download("TSLA", start="2022-10-01", end="2023-10-01")
apple = yf.download("AAPL", start="2022-10-01", end="2023-10-01")
amazon = yf.download("AMZN", start="2022-10-01", end="2023-01-01")
visa = yf.download("V", start="2022-10-01", end="2023-01-01")
dow = yf.download("dow", start="2022-10-01", end="2023-01-01")
brka = yf.download("BRK-A", start="2022-10-01", end="2023-01-01")
mstrc = yf.download("MA", start="2022-10-01", end="2023-01-01")

data1 = company1.history(period="1y")
data2 = company2.history(period="1y")
data3 = company3.history(period="1y")
data4 = company4.history(period="1y")
data5 = company5.history(period="1y")
data6 = company6.history(period="1y")
data7 = company7.history(period="1y")



st.write("""### Apple Inc. """)
st.write(apple)
st.line_chart(data2.values)
st.bar_chart(data2.values)

st.write("""### Amazon.com Inc. """)
st.write(amazon)
st.line_chart(data3.values)
st.bar_chart(data3.values)


st.write("""### Visa""")
st.write(visa)
st.line_chart(data4.values)
st.bar_chart(data4.values)


st.write("""### DOW Inc. """)
st.write(dow)
st.line_chart(data5.values)
st.bar_chart(data5.values)


st.write("""### Berkshire Hathaway Inc.  """)
st.write(brka)
st.line_chart(data6.values)
st.bar_chart(data6.values)


st.write("""### Mastercard  """)
st.write(mstrc)
st.line_chart(data7.values)
st.bar_chart(data7.values)


st.write("""### Tesla Inc. """)
st.write(tesla)
st.line_chart(data1.values)
st.bar_chart(data1.values)