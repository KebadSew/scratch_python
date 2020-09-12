from clear_console import cls as myCls
from my_module import PI as myPi, f as myF, g as myG

'''
Note: f(x)
f : is the funcation name. It is the function reference
f(5): is invoking the function. You are passing the input parameter
value of 5 and asking the function to execute

'''

# cs & mm can be considered as aliases 

myCls()

# accessing variable/attribute in my_module
print(myPi)

# accessing methods in my_module
print(myF(5))
print(myG(8,2))

