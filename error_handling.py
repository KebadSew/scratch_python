# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:03:11 2020

@author: legen
"""

from clear_console import cls 
cls()

s = '1.2345'
print(s)
print(type(s))
f = float(s)
print(f)
print(type(f))

cls()

''' 
the below is problematic code as it'll cause
an exception / error when coverting to float
#s = '1.234*ads'
print(s)
print(type(s))
#f = float(s) # causes ValueError
print(f)
print(type(f))
'''

# this catches / suppress generic 
# types of errors
def to_float(s):
    try:
        return float(s)
    except ValueError:
        return 'ValueError - unable to convert', s
    
s = '1.2345'
print(to_float(s))
s = '1.234.5'
print(to_float(s))

'''
s = 1,2
f = float(s) # causes TypeError
print(f)
'''


def to_float2(s):
    try:
        return float(s)
    except TypeError:
        return 'TypeError - unable to convert', s
s = 1,2
f = to_float2(s) # causes TypeError
print(f)

def to_float3(s):
    try:
        return float(s)
    except (ValueError,TypeError):
        return 'Unable to convert',s

s = '1.2345'
print(to_float3(s))
s = '1.234.5'
print(to_float3(s))
s = 1,2,4
print(to_float3(s))




