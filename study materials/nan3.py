# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 23:27:22 2018

@author: nandavari
"""

def bsort (mlist):
    for passnum in range(len(mylist)-1,0,-1):
        if mlist[i]>mlist[i+1]:
            mlist[i] =mlist[i]+mlist[i+1]
            mlist[i+1] =mlist[i]-mlist[i+1]
            mlist[i]=mlist-mlist[i+1]
            mylist = [12,13,15,35,34,32,17]
            bsort(mylist)
            print(mylist)
            
            
            
            ##selection sort
            
            
def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


l = [19,2,31,45,30,11,121,27]
selection_sort(l)
print(l)            
    