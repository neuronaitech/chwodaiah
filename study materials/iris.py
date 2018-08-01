# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:50:04 2018

@author: nandavari
"""

from sklearn import svm
from sklearn import datasets
from sklearn import preprocessing
iris=datasets.load_iris()
clf=svm.LinearSVC()
x=clf.fit(iris.data,iris.target)
clf.predict([[10.0,13.6,5.3,3.25]])
vlt=clf.coef_
print(vlt)
X =iris.data
Y =iris.data
std_scale = preprocessing.StandardScaler().fit(X)
X_train_std = std_scale.transform(X)
print(X_train_std)
X_test_std  = std_scale.transform(Y)
print(X_test_std)