def greet(name, age):
    print(F"hello {name}, you are {age} year's old")

greet("akka", 26)

#task:- 2
def greet(name, age):
    print(F"hello {name}, you are {age} year's old")

greet(age= 26, name= "akka")

#task:- 3
def greet(name, age = 25):
    print(F"hello {name}, you are {age} years old.")

greet("megha")
greet("mahi", 21)   
greet("jhgh",766)
greet("hghju",665)

#task:-4
def print_num(*args):
    for numbers in args:
        print(numbers)

print_num(1,2,3,4,5)

#task:- 5
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(F"{key}: {value}")

print_info(name="kumar", profession = "engineer")
print_info(country= "india", population= 1300000, capital= "new delhi")


#task:-6
def mixed_arguments(a, b=2, *args, **kwargs):
    print(f"a:{a}")
    print(f"b:{b}")
    print("args:",args)
    print("kwargs:-",kwargs)

mixed_arguments(1,2,4,8,x=10, y=20)
