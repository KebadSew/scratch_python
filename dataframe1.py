# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:26:40 2020

@author: legen
"""

from clear_console import cls 
import numpy as np
import pandas as pd

cls()

arr = [9889,32,321, 10293, 182830]

for i,val in enumerate(arr):
    print('i={0} val={1}'.format(i, val))
    
v = pd.Series(arr)
print(v)
print(v.values)
print(v.index)
cls()

d = {'a':100,'b':200,'c':300}
s = pd.Series(d)
print(s)

lables = ['c','a','z','b']
s = pd.Series(d,index=lables)
print(s)

data = {
        'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data, columns=['year', 'pop', 'state'])
print(frame)

print(frame['state'])
#frame = pd.DataFrame(data)

cls()

data = [4.5, 7.2, -5.3, 3.6]
indexes = ['d', 'b', 'a', 'c']
columns=['one','two','three','four']

obj = pd.Series(data)
print(obj)
obj = pd.Series(data,index=indexes)
print(obj)
cls()
data2 = {'a':[4.5], 'b': [7.2],'c': [-5.3], 'd':[3.6]}
frame = pd.DataFrame(data2,columns=indexes)
print(frame)
cls()
data2 = np.arange(16).reshape((4,4))
frame = pd.DataFrame(data2,index=indexes,columns=columns)
print(frame)

print(frame['three'])# to access the columns
print(frame.loc['b']) # to access the row

cls()
print(frame)
frame['five'] = frame['two'] <= 5
print(frame)
frame['sum'] = frame['one']+frame['two']+frame['three']+frame['four']
print(frame)
cls()
frame.loc['e'] = frame.loc['d'] + frame.loc['b']+ frame.loc['a']+ frame.loc['c']
frame['five'] = frame['two'] <= 5
print(frame)

del frame['five']
print(frame)
print('three' in frame.columns)
print('b' in frame.index)
cls()

print(obj)
series2 = obj.reindex(['a','b','d','c'])
print(series2)
print(series2.drop(['d','b']))

cls()

print(frame)
#print(frame[['three','sum']])

print(frame.drop(['two','sum'],axis='columns')) #columns .. axis=1

cls()
print(frame)
print(frame.loc[['c','e'],['two','sum']])
print(frame.iloc[[3,4],[1,4]])
print(frame.iloc[2])




















