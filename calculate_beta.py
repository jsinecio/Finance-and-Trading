# -*- coding: utf-8 -*-

"""
@author: jesux

 This code in python is useful to calculate share's beta coefficient in a stock market.
 Beta coefficient returns a value that shows if the share of a company is defensive or if is not.
 Values above 1 means that the share is volatile; values below 1 means that the share is conservative.
 Meanwhile returned values equal to 1 represent that the share has a similar behavior to the market.

## In this exmaple I'm getting the share of Walmart and the Standard and Poors 500 (S&P500)
"""
import yfinance as yf
import numpy as np

# Define tickers
share_ticker = "WMT"
market_ticker = "^GSPC"

# Download data
data = yf.download(tickers=[share_ticker, market_ticker], period="5y", 
                   interval="1d")['Adj Close']

# Calculate logarithm returns 
log_returns = np.log(data / data.shift(1))

# Calculate covariance between the share and the market
covariance = log_returns.cov().loc[share_ticker, market_ticker]

# Calculate la market's variance
market_variance = log_returns[share_ticker].var()

# Calculate beta
beta = covariance/market_variance
print(" ")
print("WALMART's beta:",beta)

