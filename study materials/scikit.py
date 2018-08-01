# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 23:11:32 2018

@author: nandavari
"""

from sklearn import datasets
iris=datasets.load_iris()
print(iris.data.shape)
print(iris.feature_names)
print(iris.target_names)
print(iris.target)
print(iris.DESCR)
print(iris.data)
X=iris.data
y=iris.target


##
cancer=datasets.load_breast_cancer()
print(cancer.data.shape)
print(cancer.feature_names)
print(cancer.DESCR)

##SVM
from sklearn import svm
from sklearn import datasets
iris=datasets.load_iris()
clf=svm.LinearSVC()
clf.fit(iris.data,iris.target)
clf.predict([[5.,6.,5.,6.]])
print(clf.coef_)