from clear_console import cls
import pandas as pd
import numpy as np
# cls()
#
# data = pd.Series(np.random.randn(9))
# print(data)
#
# data = pd.Series(np.random.randn(9),
#                  index=[['a','a','a','b','b','c','c','d','d'],
#                         [1,2,3,1,3,1,2,2,3]])
# print(data)
# print(data['b'])
# print(data['b':'d'])
# print(data.loc[['b','d']])
#
# print('==============')
# print(data['a':'c'])
# print(data.loc[:,1])
# print(data.loc[:,3])
# print("--------------")
# print(data['b'].loc[3])
# print(' ---- ')
# print(data.unstack())
# print(data.unstack().stack())
# print(' ---- ')
# cls()
# frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
#                      index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
#                      columns=[['Ohio', 'Ohio', 'Colorado'],
#                               ['Green', 'Red', 'Green']])
# frame.index.names = ['KEY1','KEY2']
# frame.columns.names = ['STATE', 'COLOR']
# print(frame)
# print(frame['Ohio'])
# print(frame.stack().swaplevel('KEY1','KEY2'))
# print(frame.swaplevel('KEY1','KEY2'))
# print(frame)
# print(frame.sort_index(level=1)) # sort by KEY2 b/c it on level 1 whereas KEY1 is on level 0
# print(frame.sort_index(level=0)) # sort by KEY1
#
# print(frame.swaplevel('KEY1','KEY2'))
# print(frame.swaplevel('KEY1','KEY2').sort_index(level=0))
#
# print(frame.sum(level='KEY2'))
# print(frame.sum(level='COLOR', axis=1))

frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two','two', 'two'],
                      'd':[0,1,2,0,1,2,3]})
print(frame)
frame2 = frame.set_index(['c','d'])
print(frame2)

# frame2 = frame.set_index(['c','d'],drop=False)
# print(frame2)
print(frame2.reset_index())