# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:27:29 2020

@author: legen
"""

cls = lambda: print("\033[2J\033[;H", end='')
cls()


x = "Hello World! {}" #initialization, assignment

# x references the object "Hello World!"

# example for methods, functions in str object

x = x.replace("Hello", "Tenayistilign")
print(x)

x = x.upper()
print(x)

x = x.capitalize()
print(x)

x = x.format(2020)
print(x)

x = x.upper()
print(x)

x = [1,2,3]
print(x)
x = x.clear()
print(x)
x = [4,5,6]
print(x)
print(x.pop(1))
print(x.remove(6))

cls = lambda: print("\033[2J\033[;H", end='')
cls()

# remove() removes by value but not by index
# remove() doesn't return a value

# pop() returns element and removes by index

y = [8,6,2,4,3,1,2,8,7,4,8]
print(y.count(8))
print(y.pop(7))
print(y)

print(y.remove(2))
print(y)
y.remove(2)
print(y)

y.sort()
print(y)

y.insert(0, 55)
print(y)
y.sort()
print(y)

y.reverse()
print(y)

y.append(100)
print(y)
y.sort()
print(y)

#print(y.index(7,0,5)) # will give error
print(y.index(7,0,6))



