# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:14:13 2020

@author: legen
"""

from clear_console import cls 
import numpy as np

cls()

arr = np.arange(32)
print(arr)
print(arr.reshape((8,4)))
print(arr.reshape((4,8)))
print(arr)
print(' --- ')
arr = np.arange(15).reshape((3,5))
print(arr)
arr2 = arr.T
print(arr2)
print(arr)


arr = np.empty((6,3))
for i in range(6):
    arr[i] = i
print(arr)
print(arr.T)

prod = np.dot(arr.T,arr)
print(prod)

print(' --- ')
x = np.array([[2,2,2],[2,2,2]]) #(2,3)
y = np.array([[1,2,3],[4,5,6],[7,8,9]]) # (3,3)
prod = np.dot(x,y)
print(prod)

prod = np.dot(y,x.T)
print(x.T)
print(y)
print(prod)

cls()

# Ufunc - Universal Functions

arr = np.array([2.5,3.5,-0.6,-0.95])

print(arr)

remainder, whole = np.modf(arr)
print('remainder ',remainder)
print('whole part ', whole)

print(whole[2]+1)
print(whole[2]* -1)

#print(np.sqrt(arr))
#print(np.sqrt(arr,arr)) #operates on the original array
#print(arr)

cls()

# Array-Oriented Programming with Arrays

points = np.arange(-1,1,0.5)
print(points)
xs, ys = np.meshgrid(points,points)
z = np.sqrt(xs**2 + ys**2)
print(z)
print(z.shape)


























