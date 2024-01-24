import streamlit as st
import yfinance as yf


def stock_ticker(name):
	company = yf.Ticker(name) 
	return company

st.title("StockWizzard")

st.subheader('A responsive, stock ticker data science and data analytics app. The webapp provides data on companies listed in the NASDAQ marketplace', divider='rainbow')

company1 = stock_ticker("TSLA")
company2 = stock_ticker("AAPL")


company3 = stock_ticker("AMZN")

company8 = stock_ticker("SOFI")
company9 = stock_ticker("META")


company4 = stock_ticker("V")
company5 = stock_ticker("DOW")
company6 = stock_ticker("BRK-A")
company7 = stock_ticker("MA")

tesla = yf.download("TSLA", start="2023-10-01", end="2024-10-01")
apple = yf.download("AAPL", start="2023-10-01", end="2024-10-01")
amazon = yf.download("AMZN", start="2023-10-01", end="2024-01-01")

sofi = yf.download("SOFI", start="2023-10-01", end="2024-01-01")
meta = yf.download("META", start="2023-10-01", end="2024-01-01")

visa = yf.download("V", start="2023-10-01", end="2024-01-01")
dow = yf.download("dow", start="2023-10-01", end="2024-01-01")
brka = yf.download("BRK-A", start="2023-10-01", end="2024-01-01")
mstrc = yf.download("MA", start="2023-10-01", end="2024-01-01")

data1 = company1.history(period="1y")
data2 = company2.history(period="1y")
data3 = company3.history(period="1y")

data8 = company8.history(period="1y")
data9 = company9.history(period="1y")

data4 = company4.history(period="1y")
data5 = company5.history(period="1y")
data6 = company6.history(period="1y")
data7 = company7.history(period="1y")

st.write("""### Tesla Inc. """)
st.write(tesla)

st.write("""### Apple Inc. """)
st.write(apple)

st.write("""### Amazon.com Inc. """)
st.write(amazon)

st.write("""### SoFi Inc. """)
st.write(sofi)

st.write("""### Meta Platforms """)
st.write(meta)

st.write("""### Visa""")
st.write(visa)

st.write("""### DOW Inc. """)
st.write(dow)

st.write("""### Berkshire Hathaway Inc.  """)
st.write(brka)

st.write("""### Mastercard  """)
st.write(mstrc)
