# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 11:59:28 2018

@author: nandavari
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_boston
boston = load_boston()
boston
df_x = pd.DataFrame(boston.data,columns=boston.feature_names)
df_y = pd.DataFrame(boston.target)
df_x.describe()
reg=linear_model.LinearRegression()
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,test_size=0.2,random_state=4)
reg.fit(x_train,y_train)
#weight values
reg.coef_
a = reg.predict(x_test)
y_test[0]
# mean squre error
np.mean((a-y_test)**2)
