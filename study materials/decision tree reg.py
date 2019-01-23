# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:34:45 2018

@author: nandavari
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
df = pd.read_csv('apple.csv',index_col=0)
print(df.head())
print(len(df))
X = df[['Close']].values.reshape(-1,1)
y=  np.where(df['Close'].shift( -1) >df['Close'],1,-1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(criterion='gini')
clf.fit(X_train, y_train)
p = clf.predict(X_test)


#plotting
plt.scatter(X_train,y_train,color='r')
plt.plot(X_train,clf.predict(X_train),color='y')
plt.show()