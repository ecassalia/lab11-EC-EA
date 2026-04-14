import math

<<<<<<< HEAD
def square_root(a):
    return math.sqrt(a)
    if a <0:
        raise ValueError
def hypotenuse(a,b):
    return math.hypot(a,b)
=======
#Partner 1
>>>>>>> 979e86e0736afda4c9161ef562772e27832d0d6f
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b


def logarithm(a,b):
    if a<=0:
        raise ValueError("")
    return math.log(b, a)

def exponent(a,b):
    return a**b



#Partner2
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

#Raise ZeroDivisionError
def div(a,b):
    if a == 0:
        raise ZeroDivisionError("")
    return b / a

def log(a,b):
    if a<=0:
        raise ValueError()
    return math.log(b, a)

def exp(a,b):
    return a**b
