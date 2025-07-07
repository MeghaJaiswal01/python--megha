#task 1:- 'tuple'
tuple1 = (1,2,3)
tuple2 = 'a','b','c'
tuple3 = (4,5,6)
print(tuple1,tuple2,tuple3)

#task 2
my_tuple = (10,20,30,40)
print(my_tuple[0])
# print(my_tuple[3])

# task3:-
my_tuple = (1,2,3,4,5,6)
print(my_tuple[1:3])
print(my_tuple[::2])

#task 4
my_tuple = (1,2,3)
print("tuplea are immutable")

#task 5
tuple1 = (1,2)
tuple2 = (3,4)
result = (tuple1+tuple2)
print(result)

#task 6
my_tuple = (1,2,0)
repeated = my_tuple*3
print(repeated)

# task 7 'len'
my_tuple = (1,2,3,4,5,6,7,8,9)
print(len(my_tuple))

#8
my_tuple = (1,2,3)
print(3 in my_tuple)
print(6 in my_tuple)


#9
my_tuple = (1,2,3,4,5,6,7,8,9,0)
for num in my_tuple:
    print(num)

#index
print(my_tuple.index(6))

#count
my_tuple = (1,2,3,3,4,4,4,4,4,4,5,2,1)
print(my_tuple.count(4)) 

#task12
nested_tuple = (1,(2,3),(4,(5,6)))
print(nested_tuple[1])
print(nested_tuple[2][1])

# #task13
my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)

#task14
cordinates = {(1,2):"point a", (3,4):"point b"}
print(cordinates[(1,2)])

#task15
my_tuple = (1,2,3)
my_list = [1,2,3]
my_list[0] = 5
print(my_list)

#task 16
def get_coordinates():
    return(10,20)

x,y = get_coordinates()
print(x,y)

#task17:-
tuple_list = [(3, 'C'),(1,'A'),(2,'B')]
sorted_list = sorted(tuple_list)
print(sorted_list)

#task 18
my_tuple = ()
print(hash(my_tuple))

