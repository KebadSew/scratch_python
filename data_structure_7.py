# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 08:46:51 2020

@author: legen
"""
import itertools
from clear_console import cls 
cls()

d = {'a':1, 'b':2, 'c':3}
# d is an iterable object

for key in d:
    print(key,':',d.get(key), end=' ')
    
cls()

d_iter = iter(d) 
# d_iter is just an iterator object
# list(d_iter) returns a list of the dict keys
print(list(d_iter))

cls()
# list is iterable
d2 = [1,3,4,5]
d2_iter = iter(d2)
print(list(d2_iter))

cls()
# tuple is iterable
d3 = 3,4,5,2,9
d3_iter = iter(d3)
print(list(d3_iter))

cls()

# generator
n = 10
s = list(range(1,n+1)) # sequence from 1-10
print(s)

def squares():
    n = 10
    print('Generating squares from 1 t0 {0}'.format(n**2))
    for i in range(1, n+1): # materialized 
        yield i**2
        
gen = list(squares())
print(gen)

gen = squares()

for x in gen:
    print(x, end=' ')

cls()



names = ['Alem', 'Adam','Wes','Will','Albert','Steven']
first_letter = lambda x: x[0]

def iter_():
    for x,n in itertools.groupby(names,first_letter):
        print(x,list(n))
# before sorting
iter_()

print(' --- ')

# after sorting
names.sort()
iter_()

cls()

print(' -- combinations --')
seq = list(range(1,4))
print(seq)
seq_iter = iter(seq)
comb = itertools.combinations(seq_iter, 2)
print(tuple(comb))

print(' --- ')
seq = list(range(1,5))
print(seq)
seq_iter = iter(seq)
comb = itertools.combinations(seq_iter, 3)
print(tuple(comb))

print(' --- ')
seq = list(range(1,5))
print(seq)
seq_iter = iter(seq)
comb = itertools.combinations(seq_iter, 2)
print(tuple(comb))

print(' -- permutations --')

seq = list(range(1,4))
print(seq)
seq_iter = iter(seq)
perm = itertools.permutations(seq_iter, 2)
print(tuple(perm))

print(' --- ')
seq = list(range(1,5))
print(seq)
seq_iter = iter(seq)
perm = itertools.permutations(seq_iter, 3)
print(tuple(perm))
































