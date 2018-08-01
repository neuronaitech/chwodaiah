# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:26:30 2018

@author: nandavari
"""

import pandas as pd
df = pd.read_csv('kk.csv')
print(type(df))
print(df.shape) 
print(df.columns)
print(df.dtypes)
#	get	more	information	about	our	data
print(df.info()) 
df1=df['Volume'] 
print(df1.head(20))
print(df1.tail(10))
df1	= df[['Volume',	'Open',	'Adj Close']]
print(df1.head(10))  
print(df1.tail(7))
#print the last row index
number_of_rows	=	df.shape[0] 
last_row_index	=	number_of_rows	-	1 
print(df.loc[last_row_index]) 
#another type to print the last row 
print(df.tail(n=1)) 
#	create	a	range	of	integers	from	0	to	14	inclusive
df1	=list(range(15))
print(df1)   

subset	=df.iloc[:,:4]
print(subset.head())
#	create	a	range	from	3	to	5	inclusive
small_range	=	list(range(3,	6))
print(small_range)

subset	=	df.iloc[:,	small_range] 
print(subset.head()) 
df.index
type(df.index)
df.iloc[-5:-10,:]
import numpy as np
df.iloc[::3, -1] = np.nan
df.head(6)
low = df['Low']
type(low) 
low.head()
lows = low.values 
type(lows)
df = pd.read_csv('AAPL.csv')
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],      
      'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],    
         'visitors': [139, 237, 326, 456],            
             'signups': [7, 12, 3, 5]}
users = pd.DataFrame(data)

cities = ['Austin', 'Dallas', 'Austin', 'Dallas'] 
signups = [7, 12, 3, 5] 
visitors = [139, 237, 326, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
list_labels = ['city', 'signups', 'visitors', 'weekday']
list_cols = [cities, signups, visitors, weekdays]
zipped = list(zip(list_labels, list_cols))
print(zipped)

data = dict(zipped)
users = pd.DataFrame(data)  

users['fees'] = 0 # Broadcasts to entire column 
#broadcast with a dict
heights = [ 59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1 ] 
data = {'height': heights, 'sex': 'M'}
results = pd.DataFrame(data) 

#index and columns
results.columns = ['height (in)', 'sex']
results.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

#plotting with pandas
import pandas as pd 
import matplotlib.pyplot as plt 
aapl = pd.read_csv('aapl.csv', index_col='Date',parse_dates=True) 
aapl.head(6)
close_arr = aapl['Close'].values 
type(close_arr)
plt.plot(close_arr)
plt.show()

#plotting series
close_series = aapl['Close']
print(close_series)
plt.plot(close_series)
plt.show() 
#another plotting series
close_series.plot()  # plots Series directly
plt.show()
#plotting dataframes
aapl.plot()  # plots all Series at once
plt.show()

plt.plot(aapl) # plots all columns at once
plt.show()

#fixing scales
aapl.plot()
plt.yscale('log') # logarithmic scale on vertical axis
plt.show()

#customizing plotting
aapl['Open'].plot(color='b', style='.-', legend=True)
aapl['Close'].plot(color='r', style='.', legend=True)
plt.axis(('2018','2017',10))
plt.show()

#saving plotting
aapl.loc['2017':'2018',['Open', 'Close', 'High','Low']].plot()
plt.savefg('aapl.png')
plt.savefig('aapl.jpg')
plt.savefig('aapl.pdf')
plt.show()
 


      