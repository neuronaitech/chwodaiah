# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 21:26:30 2018

@author: nandavari
"""
#interpolate 
from scipy.interpolate import interp1d
import numpy as np
x = np.linspace(0, 10, num=10, endpoint=True)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 10, num=1001, endpoint=True)
import matplotlib.pyplot as plt
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()

#coefficent
import cmath
a = int(input("enter a value:"))
b =int( input("enter b value:"))
c =int( input("enter c value:"))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))