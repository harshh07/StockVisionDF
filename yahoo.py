import yfinance as yf
import ssl
import matplotlib.pyplot as plt
import csv
import pandas as pd
import datetime as dt

print("Following Tickers are:")
print("1. CIPLA.NS")
print("2. RELIANCE.NS")
print("3. TATAMOTORS.NS")
print("4. VEDL.NS")
print("5. LT.NS")
tick=input("Enter the Ticker: ")
comp = yf.Ticker(tick)
#Get Historical Market Data
hist = comp.history(period="1y")
print(hist)
start = dt.datetime(2020,1,1)
end = dt.datetime.now()

#Download Stock Data then export as CSV
data_df = yf.download(tick, start, end)
filename='Stocks_dataset/'+tick+'.csv'
data_df.to_csv(filename)


