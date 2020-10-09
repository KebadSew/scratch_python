# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:37:49 2020

@author: legen
"""

from clear_console import cls 
cls()

seq =list(range(1,10))
print(seq[::-1])
print(seq[::2])
print('seq=',seq)

print('----')

i=0
for x in seq:
    print(i, end=' ')
    i +=1
    
print('\n-----')

for x in seq:
    print(x, end=' ')

print('\n -----')

i = 0
for x in seq:
    print('i={0} seq[i]={1} x={2}'.format(i, seq[i],x))
    i +=1
    
print('\n----')
 
for i,x in enumerate(seq):
    print('i={0} seq[i]={1} x={2}'.format(i, seq[i],x))

seq = ['a','b','c','d','e']
mapping= {}

for i,x in enumerate(seq):
    mapping[x]= i

print(mapping)

mapping = {} #reset
for i,x in enumerate(seq):
    mapping[i]= x
    
print(mapping)

print(' --- ')

seq = list(range(1,10))[::-1]
print(seq)
seq = sorted(seq)
print(seq)

cls()

seq1 = list(range(1,4))
seq2 = ['a','b','c']
zipped = zip(seq1,seq2)
zipped = list(zipped)
print(zipped)
print(len(zipped))

for i,x in enumerate(zipped):
    print(zipped[i], end=' ')

cls()

seq1 = list(range(1,4))
seq2 = ['a','b']
zipped = zip(seq1,seq2)
zipped = list(zipped)
print('seq1=',seq1)
print(zipped)

cls()

seq1 = list(range(1,4))
seq2 = ['a','b','c']
zipped = zip(seq1,seq2)
zipped = list(zipped)
print('seq1=',seq1)
print('seq2=',seq2)
print(zipped)

for i,(x,y) in enumerate(zipped):
     print('i={0} zipped[i]={1} x={2} y={3}'.format(i, zipped[i],x,y))
     print('{0}: {1}, {2}'.format(i,x,y))

cls()

seq = list(reversed(list(range(1,10)))) #materialized
print(seq)
seq = sorted(seq)
print(seq)

cls()

seq = [('a','d'),('b','e'),('c','f')]
x,y = zip(*seq)
print(x)
print(y)












