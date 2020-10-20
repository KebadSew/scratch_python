# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:11:14 2020

@author: legen
"""

from clear_console import cls 
cls()

path = 'files/hello.txt'
f = open(path)
for line in f:
    print(line)
f = open(path)

lines = [line.rstrip() for line in f]
print(lines)
f.close()

lines=''
with open(path) as f:
    lines = [line.rstrip() for line in f]
print(lines)

# FileExistsError
#path = 'files/hello.txt'
#f = open(path, 'x')

# New file - becareful of overwritting!
path = 'files/hello2.txt'

with open(path, 'w') as f:
    f.write('hello hello\n')
    f.write('Sueña el r')

with open(path) as f:
    lines = [line.rstrip() for line in f]
    print(lines) 
    print(f.tell())

with open(path) as f:
    print(f.read(5))    
    print(f.read())
    print(f.tell())
   
with open(path,'rb') as f: #binary mode
    print(f.read())
