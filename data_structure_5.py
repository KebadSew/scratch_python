# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:27:08 2020

@author: legen
"""

from clear_console import cls 
from collections import defaultdict

cls()


seq = list(range(10))
print(seq)
print(5 in seq)
print(10 not in seq)
print(seq[:2])

d = {} #empty dictionary
print(d)

d = {'a':1,'b':2,'c':3}
print(d)
print(d['a'])
print(d['b'])

'''
Example: 
    Create a dictionary that contains 
    the name of country as key and 
    capital city as value
'''

d = {'USA':'DC', 'Ethiopia':'A.A',
     'Kenya': 'Nairobi', 'Nigeria':'Lagos'}
#what's the capital city of Ethiopia
print(d['Ethiopia'])
print(d['USA'])

print('Lagos' in d)
print('Nigeria' in d)

print(' ------ ')
print('Canada' in d)
d['Canada'] = 'Otawa'
print(d)
print('Canada' in d)
print(d['Canada'])
print('Otawa' not in d) # Otawa is not a key

cls()
print(' ---- ')
print(d.keys())
print(d.items())

d['Canada'] = 'Toronto' #updating

print(' ---- ')

keys = list(d.keys())
print(keys[0])

values = list(d.values())
print(values[3])

a = [1,2,3]
b = ['a','b','c']

z = zip(a,b)
print(list(z))

cls()

c = zip(keys, values)
print(list(c))
print(' --- ')
print(d.items())

cls()

d.update({'USA':'NY', 'Kenya':'Mombassa'})
print(d)

cls()

print(d)
print(d.pop('USA'))
print(d)
print(d.get('USA','DC'))
print(d.get('Ethiopia'))
print(d.pop('Ethiopia'))
print(d)

cls()

'''
Example: Create a dict of works that begin
with a given letter (categorize)

input: ['apple', 'bat', 'bar', 'atom', 'book']
expected output: {'a':['apple', 'atom']
                  'b':['bat','bar','book']}
'''

words = ['apple', 'bat', 'bar', 'atom', 'book']
d = {}

for word in words:
    key = word[0]
    if key not in d:
        d[key] = [word] # first time entry, creates list
    else:
        d[key].append(word) # key exists, appends object

print(d)

cls()

for word in words:
    key = word[0]
    d.setdefault(key,[]).append(word)
print(d)

cls()

d1 = {}
d2 = defaultdict(list)
print('d1=', d1)
print('d2=',d2.items())


print(' --- ')
#reset
d = defaultdict(list)

for word in words:
    key = word[0]
    d[key].append(word)
    
print(d)

cls()


d = {'a':1, 'b':2}
t = {'my_dict':d,'hello':'world'}
print(t)












