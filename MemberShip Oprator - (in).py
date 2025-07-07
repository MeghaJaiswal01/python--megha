#variables
x = [1,2,3]
y = [1,2,3]
z = x

print(F"x is y: {x is y}")
print(F"x is z: {x is z}")
print(F"x is not y: {x is not y}")
print(F"z is not x -{z is not x}")

#membership 
#de3fine value and sequence
sequence = [1,2,3,4,5]
value = 4
value_n = 7
print(F"{value} in not sequence :- {value not in sequence}")
print(F"{value} in sequence {value in sequence}")
print(F"{value_n} in sequnce {value_n in sequence}")

#additonal example with strings
string = "hello world" 
megha = 'h'
meera = 'b'
print(F"{megha} in string:- {megha in string}")
print(F"{meera} not in string:- {meera  in sequence} ")