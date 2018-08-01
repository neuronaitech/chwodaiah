# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:04:08 2018

@author: nandavari
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import style
#import matplotlib.finance
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
df = pd.read_csv('MSFT.csv',parse_dates=True,index_col=0)
#df['top'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

#print(df_ohlc.head())

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
print(df_ohlc.head())



ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()
