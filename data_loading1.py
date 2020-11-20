# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:30:08 2020

@author: legen
"""

from clear_console import cls 
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

cls()

path = 'files/example.csv'

df = pd.read_csv(path)
print(df)
print(df.iloc[1])

print('-----')

df = pd.read_table(path, sep=',')
print(df)

print('-----')

df = pd.read_csv(path, index_col='message')
print(df)
print(df.loc['world'],end=' ')

cls()

path = 'files/csv_mindex.csv'
df = pd.read_csv(path,index_col=['key1','key2'])
print(df)

path = 'files/example_2.txt'
df = pd.read_table(path, sep='\s+')
print(df)

cls()

path = 'files/example.csv'
df = pd.read_csv(path, skiprows=[3,4])
print(df)
print(pd.isnull(df))

sentinels = {'b':[6]}
df = pd.read_csv(path,skiprows=[3,4], na_values=sentinels)
print(df)













