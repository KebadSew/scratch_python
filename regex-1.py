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


import re

text = """Dave dave@google.com
    Steve steve@gmail.com
    Rob rob@gmail.com
    Ryan ryan@yahoo.com
    """
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

# re.IGNORECASE makes the regex case-insensitive
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text))
m =regex.search(text)
email = text[m.start():m.end()]

print(email)



# text = """Dave dave@google.com
# Steve steve@gmail.com
# Rob rob@gmail.com
# Ad adem@gmail.com
# Ryan ryan@yahoo.com"""
#
# fname_pattern = r'[A-Z]{1}[a-z]+'
# fname_regex = re.compile(fname_pattern)
# print(fname_regex.findall(text))

