# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 20:09:20 2020

@author: legen
"""

from clear_console import cls 
import bisect

cls()


c = [1,9,2, 2, 2, 3, 4, 7]
print(bisect.bisect(c, 8))
