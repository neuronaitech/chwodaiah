# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:00:45 2018

@author: nandavari
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
#from sklearn.preprocessing import MinMaxScaler
df= pd.read_csv('MSFT.csv',index_col=None)
x=df['Close'].values.reshape(-1,1)
x=preprocessing.scale(x)
#x=preprocessing.normalize(x)
y=  np.where(df['Close'].shift( -1) >df['Close'],1,-1)
split=int(0.5*len(df))
x_train,x_test,y_train,y_test = x[:split],x[split:],y[:split],y[split:]
#cross_val = cross_val_score(LogisticRegression(),x,y,scoring='accuracy')
#print('crossvalidation'+'\n',cross_val.mean())
lr=LogisticRegression()
lr = lr.fit(x_train,y_train)
accuracy_train = accuracy_score(y_train,lr.predict(x_train))
accuracy_test = accuracy_score(y_test,lr.predict(x_test))
print('\n Train Accuracy={: .2f}%'.format(accuracy_train*100))
print('\n Test Accuracy={: .2f}%'.format(accuracy_test*100))

plt.plot(df.index,x[:,0])
plt.scatter(df.index,y)
plt.show()

#plt.scatter(x_test,lr.predict(x_test))
#plt.show()
