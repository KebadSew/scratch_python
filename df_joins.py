import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
print(pd.merge(df1,df2))
print(pd.merge(df1,df2, on='key'))


df1 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df2 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
print(pd.merge(df1,df2, left_on='lkey', right_on='rkey'))
print(pd.merge(df1,df2,left_on='lkey', right_on='rkey', how='outer'))
