# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:15:55 2018

@author: nandavari
"""
import pandas as pd
dataset = pd.read_csv('MSFT.csv')
df=dataset.iloc[:,:].values
z=pd.DataFrame(df)
