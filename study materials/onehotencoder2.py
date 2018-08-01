# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:29:49 2018

@author: nandavari
"""
import numpy as np
def one_hot_encode(x, n_classes):
    return np.eye(n_classes)[x]
def main():
    list = [0,1,2,3,2,1,0]
    n_classes = 4
    one_hot_list = one_hot_encode(list, n_classes)
    print(one_hot_list)

if _name_ == "_main_":
    main()
