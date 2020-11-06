# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:13:43 2020

@author: legen
"""

from clear_console import cls 
import numpy as np
import matplotlib.pyplot as plt
import random

cls()

# Expressing Conditional Logic As Array Operations
x = 5
y = True if x<=5 else False
print(y)

xarr = np.array([1,2,3,4,5])
yarr = np.array([6,7,8,9,10])
condarr = np.array([True, False, True, True, False])


result = [(x if c else y)
           for x,y,c in zip(xarr, yarr,condarr)]

print(result) #output [1, 7, 3, 4, 10]

result = []
# Using for loop
for i, c in enumerate(condarr):
    if(c == True):
        result.append(xarr[i])
    else:
        result.append(yarr[i])
print(result)
        

# Using numpy.where

r = np.where(condarr,xarr,yarr)
rr = np.where(condarr,xarr,yarr)
print(r)
print(rr)


r = np.where(r >=5, 100, -100)
print(r)


r = np.where(rr >=5, 100, rr)
print(r)

# Unique 

letters = np.array(['e','a','b','a','c','d','b','a','c'])
print(letters)
print(np.unique(letters)) # sorted and unique
print(sorted(set(letters)))


# File I/O with Arrays
#Saving
path = 'files/some_file.npy' #concatenate
arr = np.arange(10)
np.save(path,arr)

#Loading
file = np.load(path)
print('file content is: ',file)

#Random Walks

position = 0
walk = []
steps = 1000
for i in range(steps):
    r = random.randint(0, 1)
    step = 1 if r else -1
    position +=step
    walk.append(position)

plt.plot(walk[:1000])













































