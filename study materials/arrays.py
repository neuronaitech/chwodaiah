# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 00:00:37 2018

@author: nandavari
"""
#create an array
arr = [10, 20, 30, 40, 50]
print(arr)

#Accessing elements of array using indexing
arr = [10, 20, 30, 40, 50]
print(arr[0])
print(arr[1])
print(arr[2])

#Accessing elements of array using negative indexing
arr = [10, 20, 30, 40, 50]
print(arr[-1])
print(arr[-2])

#length of an array using len()
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
num_brands = len(brands)
print(num_brands)

#Adding an element in an array using append()
add = ['a', 'b', 'c']
add.append('d')
print(add)


#Removing elements of an array using del, remove() and pop()
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del colors[4]
colors.remove("blue")
colors.pop(3)
print(colors)


#Modifying elements of an array using Indexing 
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
fruits[1] = "Pineapple"
fruits[-1] = "Guava"
print(fruits)


#Concatenating two arrays using + operator
concat = [1, 2, 3]
concat += [4,5,6]
print(concat)


#Repeating elements in array using * operator
repeat = ["a"]
repeat = repeat * 5
print(repeat)

#Slicing an array using Indexing
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits[1:4])
print(fruits[ : 3])
print(fruits[-4:])
print(fruits[-3:-1])