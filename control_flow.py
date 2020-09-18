# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:35:54 2020

@author: legen
"""

import clear_console as cs
cs.cls()

def between(a,b,v):
    return a>=v>=b

def calc_grade(g):
    if g >= 90:
        return "A"
    elif between(90,80,g):
        return "B"
    elif between(80,70,g):
        return "C"
    else:
        return "no grade"

print (calc_grade(75))
print (calc_grade(85))
print (calc_grade(90))
print (calc_grade(76))
    