# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 23:09:05 2018

@author: nandavari
"""
from scipy.stats import norm
import numpy as np
print (norm.cdf(np.array([1,-1, 0, 1, 3, 4, -2, 6])))

#To find the median of a distribution, we can use the Percent Point Function (PPF), which is the inverse of the CDF
from scipy.stats import norm
print( norm.ppf(0.5))

#To generate a sequence of random variates  use size keyword args
from scipy.stats import norm
print (norm.rvs(size = 5))

#Uniform Distribution
#uniform distribution can be generated using the uniform function
from scipy.stats import uniform
print (uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4))

#ttest_1samp
from scipy import stats
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
print (stats.ttest_1samp(rvs,5.0))

