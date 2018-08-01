# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:54:23 2018

@author: nandavari
"""
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as pl
from sklearn.metrics import accuracy_score
#from sklearn.metrics import classification_report
actual = [-1, -1, 0, -1, 0, -4, -1, 0, -8, 0]
predicted = [-1, 0, 0, -2, 0, 0, -7, -1, -1, 0]
results = confusion_matrix(actual, predicted)
print ('Confusion Matrix :')
print(results)
print('Accuracy Score :',accuracy_score(actual, predicted))
print('Report : ')
#print(classification_report(actual, predicted))
pl.matshow(results)
pl.title('Confusion matrix')
pl.colorbar()
pl.show()





