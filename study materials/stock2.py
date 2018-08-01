# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 23:23:00 2018

@author: nandavari
"""
#the stock related data in csv format
import pandas as pd 
from pandas.tseries.offsets import MonthEnd
c = pd.read_csv('kk.csv')
print(c)
print(type(c.columns))

c['Date'] =pd.to_datetime(c['Date'])
c.set_index(c['Date'])
c['EndOfMonth'] = pd.to_datetime(c['Date'], format="%Y%m") + MonthEnd(1)
c.dtypes
print(c)
c.duplicated(subset=None, keep='first')
x=c['Adj Close']
x.plot(figsize=(13,9),label='Adj Close',legend=True,title= 'Reliance_Adjclose')










