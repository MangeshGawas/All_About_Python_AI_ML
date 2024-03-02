# Day 16: Introduction to Lists - Creation, Accessing Elements, and List Methods

my_list = [1,2,3,4,5]

mixed_list = [1,"hello", 3.14, True]

print(my_list[0])
print(my_list[3])
print(my_list[-1])
print(my_list[-2])

my_list.append(111)
last_element = my_list.pop()
print(last_element)

my_list.insert(2, 777)
print(my_list)

my_new_list = [1,12,2,3,4,5,3]
my_new_list.remove(3)
print(my_new_list)