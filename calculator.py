import math

def square_root(a):
    return math.sqrt(a)
    if a <0:
        raise ValueError
def hypotenuse(a,b):
    return math.hypot(a,b)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return b/a
    if a == 0:
        raise ZeroDivisionError
def logarithm(a,b):
    return loga(b)
    if b<=0 or a <=1:
        raise ValueError
def exponent(a,b):
    return a**b
