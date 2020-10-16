# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:29:33 2020

@author: legen
"""

from clear_console import cls 
cls()

'''
Review: Data Structure
- list: append, sort, slicing, zipping, insert, pop, remove, get
- tuple: pop, remove, get
- dict: key & value pair, create, insert, remove
- set: unordered, unique, operations: union, intersection
       difference etc

Review: Looping / Iteration
- for loop
- while loop

'''
words = ['apple', 'bat', 'bar', 'atom', 'book']
d = {}

for word in words:
    key = word[0]
    print(key, end=' ')
    d.update({key:word}) #updating / inserting to dict
print()
print(d)

cls()


#creating a dict
d = {}
d = {'a': 123, 'b': 88}

#creating a set
s = {}
s = {4,6,8,4}

print(d)
print(s)

#creating a set
s = set([2,2,2,1,4,3,3,3])
print(s)
s.add(100)
print(s)

#set operations
s1 = {4,6,5,8,3,1}
s2 = {1,5,2,9,7}

print('intersection')
print('s1 n s2', s1.intersection(s2))
print(s1 & s2)

print('union')
print('s1 u s2', s1.union(s2))
print(s1 | s2)

print('difference')
print('s1 diff s2', s1.difference(s2))
print('s2 diff s1', s2.difference(s1))

print('symmetric difference')
print(s1.symmetric_difference(s2))
# (s1 u s2) - (s1 n s2)
# {1, 2, 3, 4, 5, 6, 7, 8, 9} - {1, 5}
print(s2.symmetric_difference(s1))

cls()

s1 = {1,2,3,4}
s2 = {5,2,4,7}
s3 = {2,4}
s4 = {0,8,9,5}
print(s2.issubset(s1))
print(s3.issubset(s1))
print(s2.isdisjoint(s1))
print(s4.isdisjoint(s1))
print(s1.issuperset(s3))

cls()

#lambda

def apply(lst, f):
 return [f(x) for x in lst]

lst = [4, 0, 1, 5, 6]
v = apply(lst, lambda x: x ** 2) # [16,0,1,25,36]

print(v)

#sorting use lamda as key

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(x))
print(strings)
# ['foo', 'bar', 'card', 'aaaa', 'abab']




















