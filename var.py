# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 13:03:31 2020

@author: legen
"""

cls = lambda: print("\033[2J\033[;H", end='')
cls()

a = [1,2,3]
print(type(a))

a = 'abc'
print(type(a))

a = "abcdef"
print(type(a))

a = 123
print(type(a))

a = 100.04
print(type(a))

a = [1, 1.23, "a", 'bcd','c']
print(type(a))
print("a[0] ",type(a[0]))
print("a[1] ",type(a[1]))
print("a[2] ",type(a[2]))
print("a[3] ",type(a[3]))
print("a[4] ",type(a[4]))
