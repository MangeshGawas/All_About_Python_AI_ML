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
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            print(char, "here which of that vowels")
            count = count + 1
    return count
print(count_vowels("Hello World"))

#palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome('radar'))
print(is_palindrome('Man'))


#removing the duplicate character from the given string
def remove_duplicates(s):
    unique_chars = []
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)
    return " ".join(unique_chars)

print(remove_duplicates("hello"))

