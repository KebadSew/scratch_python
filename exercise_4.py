# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:02:22 2020

@author: legen
"""

from clear_console import cls 
cls()

#Exercise1
'''
ex. Emma is good developer. Emma is a writer
output: Emma appeared 2 times

'''

s = input("Give me input string\n")
word = 'Emma'
w = s.split(word)
print(w)
size = len(w)-1
print('Emma appeared {0} times'.format(size))

