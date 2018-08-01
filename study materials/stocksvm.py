# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:46:35 2018

@author: nandavari
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
df = pd.read_csv('MSFT.csv', header=0)
X=df[["High","Low"]]
data1 = df["High"]-df["Close"]
data2 = df["Open"]-df["Low"]
z = np.where(df['Open'].shift( -1) >df['Open'],1,-1)

#plt.xlabel('Low')
#plt.ylabel('High')
#plt.plot(X,z)
#plt.show()
# we create clusters with 100 and 50 points
rng = np.random.RandomState(0)#random number generetor
n_samples_1 = 100
n_samples_2 = 50
X = np.r_[1.5 * rng.randn(n_samples_1, 2),
          0.5 * rng.randn(n_samples_2, 2) + [2, 2]]
y = [0] * (n_samples_1) + [1] * (n_samples_2)

# fit the model and get the separating hyperplane
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(X, y)

# fit the model and get the separating hyperplane using weighted classes
wclf = svm.SVC(kernel='linear', class_weight={1: 8})
wclf.fit(X, y)

# plot separating hyperplanes and samples
plt.scatter(X[:, 0], X[:, 1], c=y,  cmap=plt.cm.Paired, edgecolors='k')
plt.legend()

# plot the decision functions for both classifiers
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 10)
yy = np.linspace(ylim[0], ylim[1], 10)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T

# get the separating hyperplane
Z = clf.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
a = ax.contour(XX, YY, Z, colors='k', levels=[0], alpha=0.5, linestyles=['-'])

# get the separating hyperplane for weighted classes
Z = wclf.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins for weighted classes
b = ax.contour(XX, YY, Z,  colors='r', levels=[0], alpha=0.5, linestyles=['-'])

plt.legend([a.collections[0], b.collections[0]], ["non weighted", "weighted"],
           loc="upper left")

plt.show()