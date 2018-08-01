# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 23:10:14 2018

@author: nandavari
"""

tup = 'python', 'geeks'
print(tup)
 
# Another for doing the same
tup = ('python', 'geeks')
print(tup)

# Code for concatenating 2 tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
 # Concatenating above two
print(tuple1 + tuple2)


# Code for creating nested tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3)

# Code to create a tuple with repetition
tuple3 = ('python',)*3
print(tuple3)

#code to test that tuples are immutable
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)

# code to test slicing
tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

# Code for printing the length of a tuple
tuple2 = ('python', 'geek')
print(len(tuple2))


#python code for creating tuples in a loop
tup = ('geek',)
n = 5  #Number of time loop runs
for i in range(int(n)):
    tup = (tup,)
    print(tup)



