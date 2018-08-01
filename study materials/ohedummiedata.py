# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:33:57 2018

@author: nandavari
"""

import pandas as pd
#from Ipython.display import display
data=pd.read_csv('AApl.csv')
print(data)
print('original feature:\n',list(data.columns),'\n')
data_dummies=pd.get_dummies(data)
print('feature after one-hotEncoding:\n',list(data_dummies.columns))