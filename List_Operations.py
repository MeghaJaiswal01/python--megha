#list 
fruits = ["apple", "bnana", "cherry","mango","orange"]
print("original list:-", fruits)

first_fruit = fruits[0]
last_fruits = fruits[-1]
print("first fruit:-", first_fruit)
print("last fruits:-", last_fruits)

#task 3
sublist_fruits = fruits[:3]
print("sublist of first three fruits:-", sublist_fruits)

#task 4:- 'append'
fruits.append("grape")
print("list after adding 'grape':-", fruits)

#task 5:- 'insert'
fruits.insert(1, "papaya" )
print("list ofter adding papaya at position '1':-", fruits)

#Task 6:-'remove'
fruits.remove("cherry")
print("list after removing 'cherry':-",fruits)

#task 7:- 'pop'
poped_fruit = fruits.pop()
print("poped fruit:-",poped_fruit)
print("list after poping :-", fruits)
  
#task 8:- 'len'
length = len(fruits)
print("num of fruits in list:-", length)

#task 9:- 'in'
is_in_list = "pineapple" in fruits
print("is 'papaya' in the list?", is_in_list)

#task10:- 'for' 'in'
print("iterating over the list:-")
for fruit in fruits:
    print(fruit)

#task 11:- 'sort', reverse
fruits.reverse()
print("list after sorting:-",fruits)

#task13:- 'for, in, if'
long_fruits = [fruit for fruit in fruits if len(fruit)<6]
print("fruits with less than six letters:-", long_fruits)

#task 14:- 'copy'
fruits_copy = fruits.copy()
print("copied list:", fruits_copy)

#task 15:- 'clear'
fruits.clear()
print("list after clearing all elements:-", fruits)

#task 16:- "extending"
vegetable =  ["carrot", "broccoli", "spinach"]
fruits_copy.extend(vegetable)
print("list ofter extending with vegetable:-", fruits_copy)

#task17:- 'count'
num_apples = fruits_copy.count("apple")
print("count of apple in the list:-", num_apples)

#task18:- 'index'
if "carrot" in fruits_copy:
    carrot_index = fruits_copy.index("carrot") 
    print("index of 'corrot':",carrot_index)  

#task 19:-
if len(fruits_copy) > 2:
    del fruits_copy[2]
print("list after removing element at index 2:-", fruits_copy) 

#task20:- 'nested list'
nested_list = [fruits_copy,vegetable]
print("nested list:-", nested_list)
