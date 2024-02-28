# Day lambda function
#sytax
# lambda argument: expression

#simple addition example
add = lambda x, y : x+y
print(add(12,3))

#map function 
numbers = [1,2,3,4,5]
squared = map(lambda x: x**2, numbers)
print(list(squared))
