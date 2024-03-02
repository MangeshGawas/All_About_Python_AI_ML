#List Manipulation Adding , removing and modifying element

#append
my_list = [1,2,3,4,5]
my_list.append(6)
print(my_list)

my_list.insert(2, 333)
print(my_list)

#pop
last_element = my_list.pop()
print(last_element)

#removing
my_list.remove(3)
print(my_list)
#modifying
my_list[2] = 100

