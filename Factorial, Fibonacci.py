def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# n = int(input("enter N:-"))
print("factorial of num:-", factorial(6))


# task:- 2
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
n = int(input("enter N:-"))
print("fiboncci number at position",n,":", fibonacci(n))
