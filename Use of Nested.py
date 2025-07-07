#use of nested
num = int(input("enter a number"))

if num >= 0:
    if num == 0:
        print(F"the number is zero.")
    else: 
        print(F"{num} is positive.")
else:
    print(F"{num} is negative.")