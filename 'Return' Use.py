def add(x,y):
    """returns the sum of two numbers"""
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError("cannot divide by zero.")
    return x / y