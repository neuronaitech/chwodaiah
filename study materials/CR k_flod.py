# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 08:32:27 2018

@author: nandavari
"""
from sklearn.model_selection import StratifiedKFold
import numpy as np

n_splits = 3

X = np.ones(10)
y = np.arange(1,11,dtype=float)
# binning to make StratifiedKFold work
yc = np.outer(y[::n_splits],np.ones(n_splits)).flatten()[:len(y)]
yc[-n_splits:]=yc[-n_splits]*np.ones(n_splits)
skf = StratifiedKFold(n_splits=n_splits)
for train, test in skf.split(X, yc):
    print("train: %s test: %s" % (train, test))
