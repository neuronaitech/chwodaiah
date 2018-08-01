# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:18:34 2018

@author: nandavari
"""
#Working of labelEncoder in sklearn
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
train = ["paris", "paris", "tokyo", "amsterdam"]
test = ["tokyo", "tokyo", "paris"]
le.fit(train).transform(test)


#Working of OneHotEncoder in sklearn
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])  

enc.n_values_
 
enc.feature_indices_
 
enc.transform([[0, 1, 1]]).toarray()




#LabelEncoder and OneHotEncoder
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# define example
data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
values = array(data)
print(values)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
# invert first example
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
print(inverted)
















