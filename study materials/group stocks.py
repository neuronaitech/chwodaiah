# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:32:30 2018

@author: nandavari
"""

#group of stocks
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as web
import datetime as dt
start = dt.datetime(2017,1,1)
end = dt.datetime.today()
stocks=['AAPL','TSLA','IBM']
df=web.DataReader(stocks,'iex',start,end)
for p_id,p_info in df.items():
    print("\n ID:",p_id)
    key = 'volume'
    for key in p_info:
        vol = df[p_id]['volume']
        d = {p_id : vol}
        stocksVol = pd.DataFrame(data = d,columns=[p_id])
        print(stocksVol)
        type(df)
        
        
