# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:16:34 2020

@author: legen
"""

from clear_console import cls 
import numpy as np

cls()

# Boolean Indexing

letters = np.array(['a','b','c','b','a'])
print(letters=='a')

data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(data)

print(data[letters=='a'])
print(' ---- ')
print(data[letters=='c'])
print(' ---- ')
print(data[letters=='b'])
print(data[(letters=='b') | (letters=='c')])
cls()


# Fancy Indexing (AKA Integer Indexing)

arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
print(arr)
print(' ---- ')
print(arr[2]) # returns 1D/List
print(arr[[2,1]]) # returns subset 1D/List
print(arr[2,1]) # returns scalar
print(arr[2][1]) # returns scalar
print(arr[[2,1],[1,2]]) # tuple of indices






