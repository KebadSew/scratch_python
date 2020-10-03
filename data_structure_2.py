# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:15:06 2020

@author: legen
"""

from clear_console import cls 
cls()

___ = "abc"
print(___)

cls()

#sequence
seq = range(0,10)
lst = list(seq)
tup = tuple(seq)

lst.append(10) # insert at the end of list
lst.insert(5, -1) #insert
lst[5] = 4.5 # in-place replacement
lst[10] = 'abc'

lst.remove(4.5) # removes the object from list
lst.remove(10)

print(lst)
print(tup)

x = tup[3]
#tup[3] = 2.5
#tup[10] = 'abc'
print(x)

cls()

x = range(-3,15)
for o in x: 
    print(o, end=' ')

cls()
print(lst)
print(lst.pop(4))
print(lst)
lst.remove('abc')
print(lst)

print('abc' in lst)
print(6 in lst)

print('abc' not in lst)
print(6 not in lst)

cls()

a = list(range(1,10))
b = list(range(20,30))

for x in b:
    a.append(x)

print(a)
print(b)

print(" --- ")

a = list(range(1,10))
b = list(range(20,30))

c = a.extend(b)
print(a)
print(b)
print(c)

#reset
a = list(range(1,10))
b = list(range(20,30))

print (" --- ")

#concatenation creates new list
c = a + b
print(a)
print(b)
print(c)

cls()

#reset
a = list(range(1,10))
b = list(range(20,30))
c = list(range(100, 120))

print(a)
print(b)
print(c)

everything = []
print(everything)

cls()

everything.extend(a)
everything.extend(b)
everything.extend(c)

#print(everything)

#reset
everything = []
#print(everything)

tup = a, b,c
for obj in tup:
    everything.extend(obj)

print("everything=", everything)

print("a=",a)
print("b=",b)
print("c=",c)

cls()
#reset
#Sorting example

a = list(range(20,30))
b = list(range(100, 120))
c = list(range(1,10))

everything =[]
tup = a, b,c
for obj in tup:
    everything.extend(obj)

#print("everything=", everything)
everything.sort(reverse=True)
print(everything)


