# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:28:42 2020

@author: legen
"""

cls = lambda: print("\033[2J\033[;H", end='')
cls()

def isString(inpt):
    return type(inpt) == str

def isNotString(inpt):
    return type(inpt) != str

def isFloat(inpt):
    return type(inpt) == float


x = "Adem"
print(isString(x))
print(isNotString(x))
x = 1.88
print(isFloat(x))



