# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:34:26 2018

@author: nandavari
"""

from operator import add
l1=[3,4,2]
l2=[4,2,5]
list=list(map(zip(add,(l1,l2))))



# matrix addition
m1 = [[1, 2, 3],
	   [4, 5, 6],
	   [7, 8, 9]]
m2 = [[10, 11, 12],
	   [13, 14, 15],
	   [16, 17, 18]]
r = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        r[i][j] = m1[i][j] + m2[i][j]
for r in r:
    print(r)
  
    
    #substraction matrix
m1 = [[10, 11, 12],
	   [13, 14, 15],
	   [16, 17, 18]]
m2 = [[1, 2, 3],
	   [4, 5, 6],
	   [7, 8, 9]]
rmatrix = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        rmatrix[i][j] = m1[i][j] - m2[i][j]
for r in rmatrix:
    print(r)
       
    
# multipication matrix     
    
A = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
B = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)    
    
    
A = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(A)):
   # iterate through columns
   for j in range(len(A[0])):
       result[j][i] = A[i][j]

for r in result:
   print(r)