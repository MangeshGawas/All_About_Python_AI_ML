# Day 19 : Introduction to tuple
#creation of tuple
my_tuple = (1,2,3,4,5)
mixed_tuple = (1,"hello",3.14,True)


#accessing Element
my_tuple = (10,20,30,40,50)
print(my_tuple[0])
print(my_tuple[2])

print(my_tuple[-1])
print(my_tuple[-2])

#tuple method
index = my_tuple.index(2)
print(index)

countMethodOutput = my_tuple.count(2)
print(countMethodOutput)
