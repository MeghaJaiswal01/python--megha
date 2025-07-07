a = 10
b = 20
c = 15
#logic and
and_result = (a < b) and (b > c)
print(f"logical and : (a < b) and (b > c): {and_result}") 

#or
or_result = (a<b) or (b>c)
print(F"logical or:  (a<b) or (b>c) : {or_result}")

#not
not_result = not(a<b)
print(F"logical not : not(a<b) : {not_result}")

#combined logical oprators
combined_result = (a<b) and (b>c) or not (c>a)
print(f"combined operators :  (a<b) and (b>c) or not (c>a) : {combined_result} ")

#additional ex. with strings
str1 = "hello"
str2 = "world"
str3 = "python"

#and with str
and_string_result = (str1 == "hello") and (str2 == "world")
print(f"and string : (str1 == 'hello') and (str2 == 'world') : {and_string_result} ")

#or with str
or_string_result = (str1 == "hello") and (str2 == "world")
print(f"logical or with str : (str1 == 'hello') and (str2 == 'world') {or_string_result}")