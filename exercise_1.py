# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:56:17 2020

@author: legen
"""

from clear_console import cls 
cls()

def sum_or_product(n1,n2):
    n1 = int(n1)
    n2 = int(n2)
    prod = n1 * n2
    summ = n1 + n2
    if(prod > 1000):
     return summ
    else:
     return prod
    
n1 = input('Provide number1: \n')
n2 = input('Provide number2: \n')

print('\nOutput: ',sum_or_product(n1, n2))


