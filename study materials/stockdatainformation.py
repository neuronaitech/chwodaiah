# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:52:33 2018

@author: nandavari
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
df = pd.read_csv('MSFT.csv',parse_dates=True,index_col=0)
df['top'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
print(df.head(15))

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['top'])
ax2.bar(df.index,df['Volume'])
plt.show()
