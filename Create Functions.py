def add(a,b):
    result = a + b
    return result


def sub(a,b):
    result = a - b
    return result 


def multiply(a,b):
    result = a * b
    return result 


def divide(a,b):
    if b != 0:
        result = a / b
    else:
        result = "cannot divide by zero" 
    return result

num1 = 10
num2 = 5

print("addition:-",add(num1,num2))
print("substraction:-",sub(num1,num2))
print("multiply:-", multiply(num1,num2))
print("divide:-", divide(num1,num2))