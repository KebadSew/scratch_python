# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 09:51:18 2020

@author: legen
"""

from clear_console import cls 
import numpy as np

cls()

# Generate some random data using numpy
data = np.random.randn(2,3) # 2 by 3 array; 2 rows / 3 columns
print(data)
data=data*2
print(data)
print(data + data)

print(data.shape)
print(data.dtype)

cls()

# Creating ndarrays (N-Dimensional Arrays)

data1 = [1, 2, 9.7, 0, 4]
data2 = np.array(data1)
print(data2)

data3 = [[8,4,2,4],[5,6,7,8]]
data3 = np.array(data3)
print('----')
print(data3)
print(data3.shape)
print(data3.dtype)
print(data3.ndim) # 2-dimensional array

print('----')
data4 = [[8,4,2,4],[5,6,7,8],[4,5,6,9],[4,5,6,9]]
data4 = np.array(data4)
print(data4)
print(data4.ndim) # 2 dimensional

cls()
# Creating ndarrays part II

data = np.zeros(10) # one dimensional
print(data)
print(data.ndim)
print(data.dtype)

data = np.zeros((2,3)) # two dimensional
print(data)
print(data.shape)
print(data.ndim)
print(data.dtype)

data = np.ones((2,3)) # two dimensional
print(data)
print(data.shape)
print(data.ndim)
print(data.dtype)

data = np.empty((2,3)) # 2 dimensional
print(data)
print(data.shape)
print(data.ndim)
print(data.dtype)
cls()

data = np.ones((2,3,2)) # 3 dimensional
print(data)
print(data.shape)
print(data.ndim)
print(data.dtype)

cls()

data = np.ones((2,3,2,2)) # 4 dimensional
print(data)
print(data.shape)
print(data.ndim)
print(data.dtype)

cls()

data = np.arange(10)
print(data)
cls()

# Example: using 'full' function
data = np.full((2,3), 8.5, float,order='C')
print(data)
print(data.astype(np.int64)) #convert to int
print(data.astype(np.int32)) #convert to int
print(data)

data = np.full((2,3), 8, np.int64,order='C')
print(data.astype(np.float)) #convert to float
print(' --- ')

data = np.eye(5) # 2x2 matrix
print(data)

data = np.identity(5)
print(data)








