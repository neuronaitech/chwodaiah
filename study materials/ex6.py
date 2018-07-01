# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 10:10:56 2018

@author: nandavari
"""
#line chart x- axis,y-axis,title,legend,annotation,xticks,xlim
import matplotlib.pyplot as plt
x=range(1,50)
y=[value *2 for value in x]
plt.plot(x,y)
xticks=([1,2,3])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Simple line plot.")
plt.plot(x,y,'g*--',label='Nandavari')
plt.legend(loc='upperrigth')
plt.xlim(1,3)
plt.show()


#pie chart of the popularity of programming Languages

import matplotlib.pyplot as plt
languages = ["java","python","php","javascript","c#","c++"]
popularity = [22.2,17.6,8.8,8,7.7,6.7]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b"]
explode = (0.1,0,0,0,0,0)
plt.pie(popularity,explode=explode,labels=languages,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("The popularity of programming Languages",color='b')
plt.axis('equals')
plt.show          


#bar
import matplotlib.pyplot as plt
languages = ["java","python","php","javascript","c#","c++"]
popularity = [22.2,17.6,8.8,8,7.7,6.7]
#colors = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b"]
xs = [i + 1 for i, _ in enumerate(languages)]
plt.bar(xs,popularity)
plt.xticks([i + 1 for i, _ in enumerate(languages)],languages)
plt.title('The popularity of programming Languages',color='r')
plt.show 


#python program to load and save image file
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.savefig('myfig')



#import numpy as np
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
y=[value *1 for value in x]
num_bins = 10
n, bins, patches = plt.hist(x, num_bins, facecolor='red',alpha=0.5)
plt.show()