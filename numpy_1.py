# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 09:15:58 2020

@author: legen
"""

from clear_console import cls 
import numpy as np
import time

cls()

my_arr = np.arange(1000000)
for _ in range(5):
 start_time = time.time()
 my_arr2 = my_arr*2
 end_time = time.time()-start_time
 print('\ntime1={0} ms'.format(int(end_time*1000)))

my_list = list(range(1000000))
for _ in range(5):    
 start_time = time.time()
 my_list2 = [x*2 for x in my_list]
 end_time = time.time()-start_time
 print('\ntime2={0} ms'.format(int(end_time*1000)))