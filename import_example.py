import clear_console as cs
import my_module as mm

# cs & mm can be considered as aliases 

cs.cls()

# accessing variable/attribute in my_module

pi = mm.PI
print(pi)

# accessing methods in my_module
resulta = mm.f(5)
resulta = resulta + 8
print(resulta)

result2 = mm.g(8,2)
x = result2 < 100
print(result2)
print(x)

x = result2 <= 10
print(x)

x = result2 > 10
print(x)
'''
Note: 
    == is a comparison operator
    =  is an assignment operator
   != is a comparision operator
'''
x = result2 == 10
print(x)

print(" ----- ")
a = [1,2,3]
b = [1,2,3]
c = [1,2,3,4]
d = [3,2,1]

print(a == b)
print(a == c)
print(a == d)

print(" ----- ")
a = 5
b = 7
c = (a == b)

print("is a == b ", c)

b = a
print("b is ", b)
print("a is ", a)

c = a == b
print("is a == b ", c)

c = (a != b)
print("is a != b ", c)

c = a is b
print("is a == b ", c)

q = "Robel"
r = "Adem"

a = q
b = r
c = a == b

print("is a == b ", c)
