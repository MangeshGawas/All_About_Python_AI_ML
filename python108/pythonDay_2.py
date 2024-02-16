# Day 2 is more like understanding data type, string manipulation and one small mini project

#Integer
x = 5
y = -10

#floats
pi = 3.14
temperature = -0.5

#String
name = "John"
message = "Hello ,World"


print(x ,end="\n")
print(y ,end="\n")
print(temperature ,end="\n")
print(message,end="\n")

#Boolean
is_python_fun = True
is_raining = False

#List
numbers = [1,2,3,4,5,6]
fruits = ["Apple","Banana", "Cherry"]

#Tuples
point=(10,20)

#Dictionaries
person = {"name":"Amit","age":24}

#Sets
unique_numbers = {1,2,3,4,5} #there is no duplicate value present in the set


#How to Manipulate String

greeting = "Hello"
name = "Alice"
full_message = greeting + ", " + name + "!"

#String Indexing and slicing
message ="Python"
first_char = message[0]
print(first_char )
substring = message[2:5]
print(substring)

#String Method
text = "   Hello , World!"
text_stripped = text.strip()
print(text_stripped)

words = text.split(',')
print(words)

#String Formatting
age = 25
formatted_message = f"My age is {age}"
print(formatted_message)

print("############mini project##########")

#Mini Project of the Day : Initial Generator

#take an user input for full Name
full_name = input("Enter your full Name:")

#split the full name into individual words
name_parts = full_name.split()


#Initialize an empty string to store initials
initials = ""

#iterate over each words in the name_part list
for name_part in name_parts:
    #add the first char of each words to the initials strng
    initials += name_part[0].upper()

#Display the initials
print("Your initials are:", initials)
