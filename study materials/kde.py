# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:35:34 2018

@author: nandavari
"""
#kernal density  Estimation¶
#Univariate estimation¶
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
x1 = np.array([-7, -5, 1, 4, 5], dtype=np.float)
kde1 = stats.gaussian_kde(x1)
kde2 = stats.gaussian_kde(x1, bw_method='silverman')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x1, np.zeros(x1.shape), 'r+', ms=20)  # rug plot
x_eval = np.linspace(-10, 10, num=200)
ax.plot(x_eval, kde1(x_eval), 'b-', label="Scott's Rule")
ax.plot(x_eval, kde2(x_eval), 'g-', label="Silverman's Rule")
plt.show()

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
def my_kde_bandwidth(obj, fac=1./5):
     """We use Scott's Rule, multiplied by a constant factor."""
     return np.power(obj.n, -1./(obj.d+4)) * fac
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x1, np.zeros(x1.shape), 'b+', ms=20)  # rug plot
kde3 = stats.gaussian_kde(x1, bw_method=my_kde_bandwidth)
ax.plot(x_eval, kde3(x_eval), 'g-', label="With smaller BW")
plt.show()