set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

print("set A:-", set_1)
print("set B:-", set_2) 

#task2:-
set_1.add(9)
set_1.remove(1)
print("set_1 after adding '9' and removing '1',", set_1)

#task3:-
union_set = set_1.union(set_2)
print("union of set 1 and set 2:-",union_set)

#task4:-
intersection_set = set_1.intersection(set_2)
print("intersection of set 1 and set 2:-", intersection_set)

#task5:-
difference_set = set_1.difference(set_2)
print("difference between set 1 and set 2:-", difference_set)
print("difference between set 2 and set 1:-", set_2.difference(set_1))

#task:-6
sym_diff_set = set_1.symmetric_difference(set_2)
print("symmeric difference of set 1 and set 2:-", sym_diff_set)

#task7:-
set_3 = {4,5}
is_subset = set_3.issubset(set_1)
print(F"is set3 is subset of set 1", is_subset)


is_superset = set_2.issuperset(set_1)
print(f"is set 2 is superset of set 1:-",is_superset)

#task:-8
is_member = 6 in set_1
print("is 6 available in set 1:-",is_member)

#task9:-
num_list = [1,1,1,2,3,5,4,6,7,9,8,8,7,6,5,5]
unique_list = set(num_list)
print("list after using keyword-'SET':-",unique_list)


#task11:-
set_1.clear()
print("set 1 after clearing:-", set_1)

#task11:-
squares_set = {x ** 2 for x in range(1,11)}
print("set of squares of numbers from 1 to 10", squares_set)