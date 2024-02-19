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

#Random library
#Project : Lottery Number Generator
import random

def generate_lottery_number():
    print("The Lottery Number GUessing")

    start = int(input("Enter the start of the range :"))
    end = int(input("Enter the end of the range:"))

    #ensure that the range is valid
    if start >= end:
        print("Invalid Range! Please enter the valid range")
        return
    #Take user input for the number of lottery no to generate
    num_numbers = int(input("How many lottery numbers to generate "))

    #ensure that the numbers of lottery numbers is valid
    if num_numbers >(end - start + 1):
        print("INvalid number of lottery number !Please enter a smaller value")
        return
    
    #Generate unique lottery numbers
    lottery_numbers = random.sample(range(start , end + 1),num_numbers)

    #sort the generated numbers
    lottery_numbers.sort()

    #Display the generate lottery number
    print("Your lottery numbers are:")
    print(lottery_numbers)

#call the function to generate lottery numbers
generate_lottery_number()

#Logic Building mini project
#Random Number Sum

numbers = [random.randint(1,100) for _ in range(5)]
total = sum(numbers)
print("Random numbers", numbers)
print("Sum of the random numbers:", total)
    
#Random Password generator
#import random

import string
def generate_password(length = 8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print("Random Password:"+ generate_password(10))

#Random element selection
my_list = ["apple", "oranges","cherry", "date"]
random_element = random.choice(my_list)
print("Prandom Element :"+random_element)