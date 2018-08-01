# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:11:20 2018

@author: nandavari
"""
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('MSFT.csv',index_col=0)
x = df.iloc[:, 1].values.reshape(-1, 1)
y = df.iloc[:, 2].values.reshape(-1, 1)

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/3,random_state=0)

"""from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)"""

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train,y_train)
y_pred = reg.predict(x_test)



#train plotting
plt.scatter(x_train,y_train,color='b')
plt.plot(x_train,reg.predict(x_train),color='r')
plt.title('microsoft datasets')
plt.xlabel('High')
plt.ylabel('Low')
plt.show()
print("score:", reg.score(x_train, y_train))

#test plotting
plt.scatter(x_test,y_test,color='b')
plt.plot(x_train,reg.predict(x_train),color='r')
plt.title('microsoft datasets')
plt.xlabel('High')
plt.ylabel('Low')
plt.show()
print("Score:", reg.score(x_test, y_test))