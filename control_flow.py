# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:35:54 2020

@author: legen
"""

import clear_console as cs
cs.cls()


def calc_grade(score):
    if score<=0:
        return None
    
    if score >= 90:
        return "A"
    elif 90>=score>=80:
        return "B"
    elif 80>score>=70:
        return "C"
    elif 70>score>=60:
        return 'D'
    else:
        return 'F'
#student scores
scores=[87,34,-23,98,100,198,68,70,80,80.01]
grades=[] #empty list

for score in scores:
    grades.append(calc_grade(score))

print(grades)

cs.cls()


#add numbers in a list
#input : list of numbers
#output : total or sum of the input numbers


numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0 #initialization

for num in numbers:
    #total = total + num
    total += num
    
print("The sum is ", total)

cs.cls()


# the continue & break keywords


#student scores
scores=[87,34,-23,98,100,198,68,70,80,80.01]
grades=[] #empty list
best_grades=['A', 'B']

for score in scores:
    if score <= 0:
        continue
    grade = calc_grade(score)
    if grade not in best_grades:
        continue
    grades.append(grade)

grades.sort()

x = 0
top_grades=[]

for g in grades:
    if(x > 2):
        break
    else:
        top_grades.append(g)
    x+=1

print(top_grades)
print(len(top_grades))

cs.cls()

for i in range(10):    
    for j in range(10):  
        if j<=9 and j%2!=0 :
            print('*',end=' ')
        else:
            print('.',end=' ')
    if i%2==0:
        print('-')
    else:
        print('^')

cs.cls()

#nested loop
for i in range(0,10): 
    print('*' * (i+1),end=' ')
    for j in range(0,10):
        if j==9:
            print('')

   
cs.cls()

ex = [(5,6),(3,2),(1,6),(11, 'hello')]
for a,b in ex:
    print("a is ",a)
    print("b is ",b)
    

























