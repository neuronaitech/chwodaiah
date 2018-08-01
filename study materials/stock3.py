# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:57:56 2018

@author: nandavari
"""
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas_datareader.data as web
style.use('ggplot')
start = dt.datetime(2017,1,1)
end = dt.datetime(2018,7,28)
stocks=['AAPL','TSLA','IBM']
df=web.DataReader(stocks,'iex',start,end)
print(df.head())

