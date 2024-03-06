# Day 23 : New Concepts
from dataclasses import replace


my_string1 = "Hello World!"
my_string2 = "Python Programming"

print(my_string1[0])
print(my_string1[-1])

# [start:end:step]

print(my_string2[1:5])
print(my_string2[7:])

# len() : its returning the lenght 

print(len(my_string1))

#lower() upper()
print(my_string1.lower())
print(my_string2.upper())

#split()
words = my_string2.split()
print(words)

# join()
words = ["python", "programming"]
sentence = ' '.join(words)
print(sentence)

# replace()
new_string = my_string1.replace('Hello', "Mangesh")
print(new_string)

#coding practice
def reverse_string(s):
    return s[::-1]

print(reverse_string("ABCD"))

#Counting vowels
def count_vowels(s):
    vowels = 'aeioAEIOU'
    count = 0
    for char in vowels:
        if char in vowels:
            count = count + 1
    return count
print(count_vowels("Hello World"))
