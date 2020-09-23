# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:29:46 2020

@author: legen
"""

from clear_console import cls 
cls()

tup = 1,2,3.5,'hello',['a','b','c']
print(tup)
tup[4].append('d')
print(tup)

nested_tup='a','b','c',(1,3,4), 'd',(6,7)
print(nested_tup)

print(tuple("mike world!")[0].upper())
print(tuple(['a','b','c']))

print(tuple("mike world!") + tuple(['a','b','c']))
print(tuple(['a','b','c'])*2)

tup = ('a','b','c')
a,b,c =  tup
print('a={0} b={1} c={2}'.format(a,b,c))

tup = 4, 5, (6, 7)
a,b,c = tup
print(c)
a,b,(c,d) = tup
print(d)
c, d = d, c
print(d)

seq = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print('a={0}, b={1}, c={2}'.format(a,b,c))


values = 1,2,3,4,5,6,7,1
print('count=',values.count(1))

a,b,*_ = values
print(_)
print(a,b)
print((a,b))


