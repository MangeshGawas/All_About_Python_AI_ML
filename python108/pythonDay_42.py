#lambda , reduce ,decorator and map

def square(x):
    return x**2
print(square(4))

#In lambda function
square_lambda = lambda x: x**2
print(square_lambda(5)) 

#Higher order function
'''
map() => map function is like iterator function containing the result

filter() => This function is used to creates iterators from element of an iterable for which a function return true

reduce() => rolling computation to sequential pairs of values in an iterable 
'''


#map(function , iterable)

numbers = [1,2,3,4,5]
triple_value = map(lambda x :x * 3 , numbers)
print(list(triple_value))


#filters 
# filter(function, iterable)

numbers = [1,2,3,4,5,6,7,8,9,10]
even = filter(lambda x:x%2==0, numbers)
print(list(even))

# reduce

# import functools
# functools.reduce(function, iterable, initlilizer)


# code
from functools import reduce
total = reduce(lambda x,y:x+y,numbers)
print(total,"Here is the total")
