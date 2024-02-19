# Lets begins the python day4

#python List
my_list = [1,2,3,4,5,6]

#accesing the elements
print(my_list[2])

#slicing lists
print(my_list[1:3])

#modifying lists
my_list[0] = 10
print(my_list)


#adding elements
my_list.append(7)
print(my_list)

#removing elements
# elements can be removed from a list by using remove() and pop() method
my_list.remove(3)

#List operation 
#+ ,*
new_list = my_list + [8,9,10]
print(new_list)

#List Methods
#sort() , reverse(), count(), index(), clear()
print(my_list.index(2))

#List comprehensions
squares = [x ** 2 for x in range(1, 6)]
print(squares)

#Nested Lists
nested_list = [[1,2,3],[4,5,6], [7,8,9]]
print(nested_list[1][2])