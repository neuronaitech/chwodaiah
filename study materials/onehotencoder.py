# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:36:44 2018

@author: nandavari
"""
#without using onehotEncoder
from sklearn import preprocessing
cat_features = ['color', 'director_name', 'actor_2_name']
#enc = preprocessing.LabelEncoder()
enc.fit(cat_features)
new_cat_features = enc.transform(cat_features)
#print ( new_cat_features) # [1 2 0]
new_cat_features = new_cat_features.reshape(-1, 1) # Needs to be the correct shape
ohe = preprocessing.OneHotEncoder(sparse=False) #Easier to read
print (ohe.fit_transform(new_cat_features))

