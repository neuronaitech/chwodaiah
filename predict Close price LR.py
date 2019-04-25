# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:59:48 2019

@author: Asus
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing,cross_validation
df=pd.read_csv('AAPLP.csv')
df=df.dropna()
df=df[['Open','High','Low','Close']]

forecast_out=int(1)
df['Prediction']=df[['Close']].shift(-1)

X=np.array(df.drop(['Prediction'],1))
X=preprocessing.scale(X)

X_forecast= X[-forecast_out:]
X=X[:-forecast_out]

y=np.array(df['Prediction'])
y=y[:-forecast_out]

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)

clf=LinearRegression()
clf.fit(X_train,y_train)

confidence=clf.score(X_test,y_test)
print("confidence:",confidence)

forecast_prediction=clf.predict(X_forecast)
print(forecast_prediction)