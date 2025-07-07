my_string = "hello, meera!"
print("original string:",my_string)
print("first character:-", my_string[5])
print("last character:-", my_string[-1])

str1 = "edunet"
str2 = "foundation"
concat_str = str1+ " " +str2
repeated_str = concat_str * 3
print("concatenated string:-", concat_str)
print("repeated string:-", repeated_str)

# task3:-
my_string = "hello, jaadu"
upper_str = my_string.upper()
print("upper_str:-",upper_str)

lower_str = my_string.lower()
print("lower string:-", lower_str) 

title_str = my_string.title()
print("title string:-", title_str)

swapcase_str = my_string.swapcase()
print("swapcase string:-",swapcase_str)


# # #task:- 4
my_string = 'hello, world' 
substring = "edunet"
found_index = my_string.find("world")
if found_index != -1:
    print(F"substring '{substring}' found at index {found_index}")
else:
    print(F"substring '{substring}' not found")

#task:- 5 'replace'
new_string = my_string.replace("hello","happy")
print("string after replacementL:-", new_string)


#TASK6:- "FORMATED string"
name = "meera"
age = 18
formatted_str = (f"my name is {name} and i am {age} years old")
print(formatted_str)

# task7:-
pedded_str = my_string.center(100,"*")
print("pedded string:-", pedded_str)

trimmed_str = "        extra spaces          ".strip()
print("trimmed string:-", trimmed_str)

#task8:- 'split'
sentense = "puyhon is fun"
words = sentense.split()
print("splitted words:-", words)



word = sentense.split()
joined_sentence = sentense.join(word)
print("joined sentence:-", joined_sentence)

#task9:- 
char_count = my_string.count("l")
print(F"character 'L' appear {char_count} times in the string")


#task10:-
is_alpha = "hello".isalpha()
print("is 'hello' alphabetic?", is_alpha)


is_digit = "1hh345".isdigit()
print("is '12h45' is numeric?", is_digit)

is_alnum = "hello123".isalnum()
print("is, 'hel123' is alphanumerical", is_alnum)


is_space = "  ".isspace()
print("is '  ' all spaces", is_space)
