# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:17:33 2020

@author: legen
"""

import clear_console as cs
cs.cls()

#Exercise: 
    # using while loop write a program that 
    # sums positive numbers less than 100
    
x = 0 #init
sum = 0 #init

while x < 100:
    sum = sum + x
    x = x + 1

print("The sum is=", sum)

#reset the variables
x = 0
sum = 0

#Sum even numbers only
while x < 100:
    if x%2==0: #remainder == 0?
        sum = sum + x
    x = x + 1

print("Sum of even numbers=",sum)


#reset the variables
x = 0
sum = 0

#Sum odd numbers only
while x < 100:
    if x%2!=0:
        sum = sum + x
    x = x + 1

print("Sum of odd numbers=",sum)

#using for loop
sum = 0
for x in range(100):
    sum += x

print("The sum using for loop is=",sum)

#even number using simple, for loop, approach

sum = 0
for x in range(0, 100, 2):
    sum +=x
    
print("The even sum using simple approach=",sum)

sum = 0
for x in range(100):
    if x%2==0:
        sum +=x
    
print("The even sum using % operation =",sum)


sum = 0
for x in range(100):
    if x%2!=0:
        sum +=x
    
print("The odd sum using % operation =",sum)

sum = 0
for x in range(1, 100, 2):
    sum +=x
    
print("The odd sum using simple approach=",sum)

cs.cls()

#Example: find index of x, if x=4. Ans: 6
#a) use for loop
#b) use while loop

y = [5,3,6,0,8,9,4,1,2]

def find_x(a):
    index = 0
    for x in y:
        if x==a:
            return index
        index+=1

print("Index of 4 is=",find_x(4))
print("Index of 4 is=",find_x(0))
print("Index of 4 is=",find_x(2))

print (" ------ ")

def find_i(a):
    size = len(y)
    print("Length of list is=",size)
    
    for i in range(size):
        if y[i]==a:
            return i
        

print("Index of 4 is=",find_i(4))
print("Index of 4 is=",find_i(0))
print("Index of 4 is=",find_i(2))

cs.cls()

#sum the elements in y
#y = [5,3,6,0,8,9,4,1,2]

#a)use for loop


sum = 0
for value in y:
    sum = sum + value
print("The sum using for loop is =", sum)

#b)use while loop

sum = 0
i = 0
size = len(y)

while i<size:
    sum = sum + y[i]
    i +=1
print("The sum using while loop is=", sum)

#reset
sum = 0
i = 0

for i in range(size):
      sum = sum + y[i]
print("The sum using for loop is=", sum)

cs.cls()
#exercise: swap the position of two number is a list
# swap first and fifth element
# input: y = [5,3,6,0,8,9,4,1,2]
# expected: y = [8,3,6,0,5,9,4,1,2]

num1 = None
num2 = None
size = len(y)

print("The list before swapping is ", y)

for i in range(size):
    if i == 0:
        num1 = y[0]
    if i == 4:
        num2 = y[4]
    
    if num1!=None and num2!=None:
        y[0] = num2
        y[4] = num1
    

print("The list after swapping is ", y)

cs.cls()

size = len(y)

print("The list before swapping is ", y)

for i in range(size):    
    if i == 4:
        temp = y[0]
        y[0] = y[4]
        y[4] = temp    
        break
    else:
        pass

print("The list after swapping is  ", y)

cs.cls()

size = len(y)

print("The list before swapping is ", y)

def swap(a, b):
    for i in range(size):    
        if i == b:
            temp = y[a]
            y[a] = y[b]
            y[b] = temp    
            
swap(0, 8)
print("The list after swapping is  ", y)

cs.cls()

z = [5,3,6,0,-1,8,9,4,1,-2]
for x in z:
    print(x,"positive" if x > 0 else "non-positive")

cs.cls()
for q in z:
    print(q,"even" if q%2==0 else "odd")





