# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 08:30:55 2018

@author: nandavari
"""

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data 
import matplotlib.pyplot as plt
import datetime as dt
start = dt.datetime(2018, 1, 1)
end = dt.datetime(2018, 8, 1)
APL = data.DataReader('AAPL', 'iex', start, end)
TSL = data.DataReader('TSLA', 'iex', start, end)
IB= data.DataReader('IBM', 'iex', start, end)

tickers = ['APL', 'TSL', 'IB']
stocks = pd.concat([APL, TSL, IB], axis = 1, keys = tickers)
stocks.head()

stocks.tail()

stocks.columns.names = ['Company', 'Stocks Data']
stocks.head()

stocks['APL']['open'].head()

stocks['APL']['high'].head()

stocks['APL']['close'].head() 

stocks.index = pd.to_datetime(stocks.index)

date = stocks.loc['2018-01-01':'2018-04-12']

stocks.plot.area(figsize = (10, 15))
 
