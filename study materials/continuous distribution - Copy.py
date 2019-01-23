# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 16:21:54 2018

@author: nandavari
"""
#alpha 
#Continuous distributions¶
from scipy.stats import alpha
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:
a = 3.57
mean, var, skew, kurt = alpha.stats(a, moments='mvsk')
#Display the probability density function (pdf):
x = np.linspace(alpha.ppf(0.01, a), alpha.ppf(0.99, a), 100)
ax.plot(x, alpha.pdf(x, a),
        'r-', lw=5, alpha=0.6, label='alpha pdf')
#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.

#Freeze the distribution and display the frozen pdf:
rv = alpha(a)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf:
vals = alpha.ppf([0.001, 0.5, 0.999], a)
np.allclose([0.001, 0.5, 0.999], alpha.cdf(vals, a))
True
#Generate random numbers:
r = alpha.rvs(a, size=1000)
#And compare the histogram:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()



#anglit Continuous distributions¶
from scipy.stats import anglit
import matplotlib.pyplot as plt
import numpy as np 
fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:
mean, var, skew, kurt = anglit.stats(moments='mvsk')
#Display the probability density function (pdf):
x = np.linspace(anglit.ppf(0.01),
                 anglit.ppf(0.99), 100)
ax.plot(x, anglit.pdf(x),
        'r-', lw=5, alpha=0.6, label='anglit pdf')
#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.
#Freeze the distribution and display the frozen pdf:
rv = anglit()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf:
vals = anglit.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], anglit.cdf(vals))
True
#Generate random numbers:
r = anglit.rvs(size=1000)
#And compare the histogram:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()



#arcsine Continuous distributions¶
from scipy.stats import arcsine
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:
mean, var, skew, kurt = arcsine.stats(moments='mvsk')
#Display the probability density function (pdf):
x = np.linspace(arcsine.ppf(0.01),
                arcsine.ppf(0.99), 100)
ax.plot(x, arcsine.pdf(x),
       'r-', lw=5, alpha=0.6, label='arcsine pdf')
#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.
#Freeze the distribution and display the frozen pdf:
rv = arcsine()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf:
vals = arcsine.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], arcsine.cdf(vals))
True
#Generate random numbers:
r = arcsine.rvs(size=1000)
#And compare the histogram:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

#argus Continuous distributions¶
from scipy.stats import argus
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:
chi = 1
mean, var, skew, kurt = argus.stats(chi, moments='mvsk')
#Display the probability density function (pdf):
x = np.linspace(argus.ppf(0.01, chi),
                 argus.ppf(0.99, chi), 100)
ax.plot(x, argus.pdf(x, chi),
       'r-', lw=5, alpha=0.6, label='argus pdf')
#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.
#Freeze the distribution and display the frozen pdf:
rv = argus(chi)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf:
vals = argus.ppf([0.001, 0.5, 0.999], chi)
np.allclose([0.001, 0.5, 0.999], argus.cdf(vals, chi))
True
#Generate random numbers:
r = argus.rvs(chi, size=1000)
#And compare the histogram:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

#beta Continuous distributions¶
from scipy.stats import beta
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:
a, b = 2.31, 0.627
mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
#Display the probability density function (pdf):
x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
ax.plot(x, beta.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='beta pdf')
#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.
#Freeze the distribution and display the frozen pdf:
rv = beta(a, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf:
vals = beta.ppf([0.001, 0.5, 0.999], a, b)
np.allclose([0.001, 0.5, 0.999], beta.cdf(vals, a, b))
True
#Generate random numbers:
r = beta.rvs(a, b, size=1000)
#And compare the histogram:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()


#betaprime Continuous distributions¶
from scipy.stats import betaprime
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:
a, b = 5, 6
mean, var, skew, kurt = betaprime.stats(a, b, moments='mvsk')
#Display the probability density function (pdf):
x = np.linspace(betaprime.ppf(0.01, a, b),
                betaprime.ppf(0.99, a, b), 100)
ax.plot(x, betaprime.pdf(x, a, b),
        'r-', lw=5, alpha=0.6, label='betaprime pdf')
#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.
#Freeze the distribution and display the frozen pdf:
rv = betaprime(a, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf:
vals = betaprime.ppf([0.001, 0.5, 0.999], a, b)
np.allclose([0.001, 0.5, 0.999], betaprime.cdf(vals, a, b))
True
#Generate random numbers:
r = betaprime.rvs(a, b, size=1000)
#And compare the histogram:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

#bradford Continuous distributions¶
from scipy.stats import bradford
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:
c = 0.299
mean, var, skew, kurt = bradford.stats(c, moments='mvsk')
#Display the probability density function (pdf):
x = np.linspace(bradford.ppf(0.01, c),
                bradford.ppf(0.99, c), 100)
ax.plot(x, bradford.pdf(x, c),
       'r-', lw=5, alpha=0.6, label='bradford pdf')
#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.
#Freeze the distribution and display the frozen pdf:
rv = bradford(c)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf:
vals = bradford.ppf([0.001, 0.5, 0.999], c)
np.allclose([0.001, 0.5, 0.999], bradford.cdf(vals, c))
True
#Generate random numbers:
r = bradford.rvs(c, size=1000)
#And compare the histogram:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

#burr Continuous distributions¶
from scipy.stats import burr
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:
c, d = 10.5, 4.3
mean, var, skew, kurt = burr.stats(c, d, moments='mvsk')
#Display the probability density function (pdf):
x = np.linspace(burr.ppf(0.01, c, d),
                burr.ppf(0.99, c, d), 100)
ax.plot(x, burr.pdf(x, c, d),
       'r-', lw=5, alpha=0.6, label='burr pdf')
#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.
#Freeze the distribution and display the frozen pdf:
rv = burr(c, d)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf:
vals = burr.ppf([0.001, 0.5, 0.999], c, d)
np.allclose([0.001, 0.5, 0.999], burr.cdf(vals, c, d))
True
#Generate random numbers:
r = burr.rvs(c, d, size=1000)
#And compare the histogram:
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()


