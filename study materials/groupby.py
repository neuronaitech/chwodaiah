# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:16:23 2018

@author: nandavari
"""

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as web
import numpy as np
stocks=['AAPL','TSLA','IBM']
df=web.DataReader(stocks,'iex')
print( df.groupby('Open'))
print( df.groupby('Date').groups)
print( df.groupby(['Open','Volume']).groups)

grouped = df.groupby('Date')

for name,group in grouped:
    print (name)
    print (group)
#aggregation
print (grouped['Open'].agg(np.mean))


grouped = df.groupby('Close')
print (grouped.agg(np.size))

print (grouped['Open'].agg([np.sum, np.mean, np.std]))

grouped = df.groupby('Date')
score = lambda x: (x - x.mean()) / x.std()*10
print( grouped.transform(score))


print( df.groupby('Open').filter(lambda x: len(x) >= 3))