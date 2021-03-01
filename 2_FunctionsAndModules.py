import random
from math import pi, sqrt #this way you only import what you need
#from math import sqrt as square_root by doing this you change the name of the import

#to use other kind of library you use pip

#to create a function use 'def'
def myfunction(word):
    print(word)

def functionthatreturn(number):
    number += 1
    return number

#like variables, functions can be assigned to variables and later referenced by those names
word = "worddd"
operation = myfunction
operation(word)

#functions can also be used as arguments of other function
def add(x, y): 
    return x + y 
    
def do_twice(func, x, y): 
    return func(func(x, y), func(x, y)) 
    
a = 5 
b = 10 
print(do_twice(add, a, b))

#example of rando module
for i in range(5):
    value = random.randint(1, 6)
    print(value)
