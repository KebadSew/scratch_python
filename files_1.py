# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:18:01 2020

@author: legen
"""

from clear_console import cls 
cls()

# Working with files

# Creating a new file, Appending etc...

path = 'files/hello.txt'
f = open(path, 'w') # write mode
f.write('Hello World!')
f.close()

path = 'files/hello.txt'
f = open(path,'w')
f.write('Hi Adem!')
f.close()

path = 'files/hello.txt'
x = open(path)
print(x.readline())
x.close()

path = 'files/hello.txt'
x = open(path,'r')
print(x.readline())
x.close()

'''
# FileExistsError
path = 'files/hello.txt'
x = open(path,'x')
x.write('Hi Robel!')
x.close()
'''
path = 'files/hello.txt'
f = open(path,'a')
f.write('\nHi Robel!')
f.close()

path = 'files/hello.txt'
f = open(path,'a')
f.write('\nHi Mike!')
f.close()

cls()

with open(path,'r') as f:
    print(f.read())
cls()

path = 'files/harlem.txt'

with open(path,'r') as f:
    print(f.readlines())
print(' --- ')
with open(path,'r') as f:
    print(f.read())
cls()

path = 'files/language.txt'
with open(path,'rb') as f:
    data = f.read()
    print(data)
    data = data.decode('utf8')
    print(data)
    
    
    
    