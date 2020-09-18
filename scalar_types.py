# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:23:16 2020

@author: legen
"""

import clear_console as cs

cs.cls()

a = None
b = None
print(a==None)
print(b==None)

c = """
For instance, I can put
all these lines in a
single variable
"""
print(c)
print(c.count('\n')) #newline
print(c.count(' ')) #space
print(c.count(','))#comma

cs.cls()

a = 100.5 #float
b = str(a)
print(type(a))
print(a*5)
print(type(b))
print(b[:3])#slicing
print(b*5)

cs.cls()

# use escaping
# \t tab
# \n new line

print("\texample \n\n\n\n\n")
print('no tabs')
print('\tend of new lines')

# to display the actual \
# use double \\
    
print('4\\2 =', 4/2)
print('4\\2 =', 4/2)
cs.cls()

s = r'4\2 ='
#print(s)

s = 'hi '
a = 'Adem! '
b = s + a
print(b * 5)

template = '{0:.2f} {1:s} are worth US${2:d}'

print(template.format(4.5560, 'Argentine Pesos', 1))

print("Hi {}".format(a))

cs.cls()
print(bool(1))

cs.cls()

a = None
b = None
c = 100
print(a is None)
print(b is None)
print(a is b)
print(a is not c)
print(c == 100)
print(c != 50)
print('a!=c',a != c)
print('a!=b',a != b)
print(type(a))















