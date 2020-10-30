# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:08:41 2020

@author: legen
"""

from clear_console import cls 
cls()

'''
input: any string
output: display character at even index of the input 

ex. 'hello' > 'h','l','o'

'''
#s = input("Input any String\n")

#for i, val in enumerate(s):
 #   if(i%2==0): #even index
 #       print(val,end=', ')
#######################################################################
# Exersise 2
'''
input: somestring, 3
expected: remove characters from index 0 up to 3 (excluding 3)
output: estring
'''

#s = input("Input another string \n")
#n = input("index of characters to remove \n")
# =============================================================================
# n = int(n)
# 
# seq = []
# for i,val in enumerate(list(s)):
#     if(i>=n):
#         seq.append(val)
# print(seq)
# =============================================================================
      
# Exercise 3
# Given a list of numbers, return True if first and last number of a list is same

def toList(str):
    ls = []
    for val in str:
        if(val != ','):
            ls.append(val)
    return ls


n = input("Give me a list of integers\n")
n = toList(n)
size = len(n)

first = n[0]
last = n[size-1]

print(first == last)


