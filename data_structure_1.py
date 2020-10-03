# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:12:59 2020

@author: legen
"""

from clear_console import cls 
cls()

a = [1,2,3,'abc',5.8, [9,10]]
# how may elements? 6
# what is the first element? 1
# what is the sixth element? [9,10] - list 

print(a[5]) #accessing 6th element using its index

# what is the first member of the sixth element? 9
# using its index
print(a[5][0])
print(a[5][1])

cls()

# using for loop
# unpack the list 

for x in a:    
    if type(x)==list:
     for y in x:
      print(y)
    else:
     print(x)
     
cls()

# using tuple

t = 1,2,3,'abc',5.8,(9,10)

for x in t:    
    if type(x)==tuple:
     for y in x:
      print(y)
    else:
     print(x)

# using its index
print(t[5][0])
print(t[5][1])

cls()

a,b,c,*r = 1,2,3,4
print(r)

cls()

a,b,c,*r = 1,2,3,'abc',5.8,(9,10)
print(r)
print(r[0])
print(r[2][1])

cls()

t = [1,2,3],4,5,6,(7,8,9)
print(len(t))
print(t[0])

t[0].append(100)
print(t[0])
print(t)
print(len(t))

cls()

# swapping variables
a,b = 1,2
print(a,b)
a,b = b,a
print(a,b)

cls()

# unpacking tuples using for loop
t = 1,2,3
for x in t:
    print(x)
cls()

t = (1,2),(3,4),(5,6)
for x,y in t:
    print(x, y)
cls()

t = (1,2),(3,4,5),(7,8,9,10)
for x,*r in t:
    print('x={0} r={1}'.format(x, r))

cls()

t = 1,2,3,3,3,4,6,4,6,6,7,3
print(t.count(3))

cls()

#Exercise: Write a program that counts how many times
# a number appears in a list/tuple

t = 1,2,3,7,3,3,4,6,4,6,6,7,3,6,1
z = 100
g = "abcdef"
h = [1,2,3,4,7,5,6,4,2,1,7]

def count_occurences(data, num):
    c = 0
    
    if type(data) == tuple or type(data) == list: 
        for x in data:
            if(x == num):
                c = c + 1
        return c
    else:
        return 0

y = count_occurences(h, 7)
print(y)
y = count_occurences(t, 3)
print(y)

cls()

