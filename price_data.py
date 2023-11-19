# Pipeline file for extracting and ingesting ticker price data
# Imports
import pandas as pd
import numpy as np
import yfinance as yf
from typing import List

# User Defined Functions
def get_ticker_data(tickers: List):
    df = yf.download(tickers, period='1d', threads=True)
    return df

def organize_ticker_data():
    pass

def ingest_ticker_data():
    pass

def execute_pipeline(tickers):
    prices = get_ticker_data(tickers)
    print(prices.head())

# Script Execution
if __name__ == "__main__":
    tickers = ['AAPL','GOOG','TSLA','MSFT','NVDA','AMD']
    execute_pipeline(tickers)
