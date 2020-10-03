# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:22:19 2020

@author: legen
"""


from clear_console import cls 
cls()

x = [1,2,3,[4,5]]

print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[3][0])
print(x[3][1])

#cls()

x = [1,2,3,[4,5,[6,7]]]

print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[3][0])
print(x[3][1])
print(x[3][2])
print(x[3][2][0])
print(x[3][2][1])

cls()


def print_list(s):
    if type(s)==list:
        for r in s:
            print(r)
    else:
        print(s)


#unpacking
for e in x:
    if type(e)==list:
        for s in e:
             print_list(s)
    else:
        print(e)

cls()




x = [1,2,3,[4,5,[6,7,[0,[8]]],8],9]
#unpacking using recursion

def unpack(x):   
 for e in x:
     if type(e) == list:
         unpack(e)
     else:
         print(e)    
         
unpack(x)
cls()
    





