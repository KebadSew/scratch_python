# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:26:40 2020

@author: legen
"""

from clear_console import cls 
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

cls()

arr = [9889,32,321, 10293, 182830]

for i,val in enumerate(arr):
    print('i={0} val={1}'.format(i, val))
    
v = pd.Series(arr)
print(v)
print(v.values)
print(v.index)
cls()

d = {'a':100,'b':200,'c':300}
s = pd.Series(d)
print(s)

lables = ['c','a','z','b']
s = pd.Series(d,index=lables)
print(s)

data = {
        'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data, columns=['year', 'pop', 'state'])
print(frame)

print(frame['state'])
#frame = pd.DataFrame(data)

cls()

data = [4.5, 7.2, -5.3, 3.6]
indexes = ['d', 'b', 'a', 'c']
columns=['one','two','three','four']

obj = pd.Series(data)
print(obj)
obj = pd.Series(data,index=indexes)
print(obj)
cls()
data2 = {'a':[4.5], 'b': [7.2],'c': [-5.3], 'd':[3.6]}
frame = pd.DataFrame(data2,columns=indexes)
print(frame)
cls()
data2 = np.arange(16).reshape((4,4))
frame = pd.DataFrame(data2,index=indexes,columns=columns)
print(frame)

print(frame['three'])# to access the columns
print(frame.loc['b']) # to access the row

cls()
print(frame)
frame['five'] = frame['two'] <= 5
print(frame)
frame['sum'] = frame['one']+frame['two']+frame['three']+frame['four']
print(frame)
cls()
frame.loc['e'] = frame.loc['d'] + frame.loc['b']+ frame.loc['a']+ frame.loc['c']
frame['five'] = frame['two'] <= 5
print(frame)

del frame['five']
print(frame)
print('three' in frame.columns)
print('b' in frame.index)
cls()

print(obj)
series2 = obj.reindex(['a','b','d','c'])
print(series2)
print(series2.drop(['d','b']))

cls()

print(frame)
#print(frame[['three','sum']])

print(frame.drop(['two','sum'],axis='columns')) #columns .. axis=1

cls()
print(frame)
print(frame.loc[['c','e'],['two','sum']])
print(frame.iloc[[3,4],[1,4]])
print(frame.iloc[2])
cls()
print(frame)
df = frame
print(df.sum())
print(df.sum(axis='columns'))
df.iloc[2] = np.nan
print(df.loc['a'])
print(df.sum(axis='columns',skipna=False)) #true by default

cls()

df=df.drop(['sum'],axis=1)
df=df.drop('e')
print(df)
print(df.idxmax())
print(df.idxmin())
print(df.mean(axis=0))
print(df.mean(axis=1))
print(df.describe())

data2 = {'grade': [1,3,5,7]}
df2 = pd.DataFrame(data2, columns=['grade'])

print(df2)
print(df2.describe())


#Correlation and Covariance /// using pandas-datareader

all_data = {ticker: web.get_data_yahoo(ticker)
            for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
price = pd.DataFrame({ticker: data['Adj Close']
                      for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume']
                      for ticker, data in all_data.items()})

returns = price.pct_change()
print(returns.tail(8))
print(returns.head())
print(returns)
print(price)
print(price.describe())
price.hist(bins=1300)
plt.show()

#correlation / corr
print(returns['MSFT'].corr(returns['IBM']))
print(returns['AAPL'].corr(returns['GOOG']))
print(returns['AAPL'].corr(returns['AAPL']))
print(returns.MSFT.corr(returns.IBM))
print(returns.corr())
print(returns.cov())















