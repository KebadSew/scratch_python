# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:26:10 2020

@author: legen
"""

from clear_console import cls 
import re

cls()

# \s pattern matching for space
# + one or more
# * zero or more
# \s+ pattern matching for one or more spaces
# \n new line
# \t tab

t = "abcxdefxghi"
print(re.split('x',t))

text = "foo bar\t baz \tqux" #space, tab
arr = re.split('\s+', text)
print(arr)

space_regex = re.compile('\s+')
print(space_regex.split(text))
print(space_regex.findall(text))

print(r'C:\x') #recommended
print('C:\\x')

cls()
#Example

text = """Dave dave@google.comSteve steve@gmail.comRob rob@gmail.comRyan ryan@yahoo.com"""

pattern = r'[A-Z]+[a-z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern,flags=re.IGNORECASE)

text = """Dave dave@google.comSteve steve@gmail.comRob rob@gmail.comRyan ryan@yahoo.com"""
fname_pattern = r'[A-Z]{1}[a-z]+'
fname_regex = re.compile(fname_pattern)
print(fname_regex.findall(text))

