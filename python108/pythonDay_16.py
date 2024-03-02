#Day 16
fruits = ["apple","mango","grapes","date"]

for fruit in fruits:
    print(fruit,"here are the present fruit")

#list comprehension

squares = [x * x for x in range(10)]
print(squares)

#even Squares
even_square = [ x*x for x in range(0,10) if x%2 ==0]
print(even_square,"here are the even square") 

#Question
#Create a list called numbers containing the numbers from 1 to 10.
list1 = [x for x in range(1,11)]
print(list1)
