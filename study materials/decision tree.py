# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:04:52 2018

@author: nandavari
"""
#classification
from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
#After being fitted, the model can then be used to predict the class of samples:
clf.predict([[2., 2.]])
#Alternatively, the probability of each class can be predicted, which is the fraction of training samples of the same class in a leaf:
clf.predict_proba([[2., 2.]])


#regression
#Decision trees can also be applied to regression problems, using the DecisionTreeRegressor
from sklearn import tree
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)
clf.predict([[1, 1]])

