# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:12:02 2020

@author: legen
"""

from clear_console import cls 
cls()

seq = list(range(10))
print(seq)

for i, x in enumerate(seq):
    if(i > 0):
        summ = seq[i-1] + seq[i]
        print('Current Number {0} Previous Number {1} Sum: {2}'.format(seq[i], seq[i-1],summ))
     
