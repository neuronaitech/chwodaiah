# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:16:17 2018

@author: nandavari
"""
#without using labelencoder
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit([1, 2, 2, 6])
le.classes_
le.transform([1, 1, 2, 6])
le.inverse_transform([0, 0, 1, 2]) 