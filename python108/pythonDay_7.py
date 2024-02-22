# python day 7 more about function

#function declaration
def greet(name):
    print("Hello", name)

#call function
greet("Mangesh")

#function Parameter
def add(a,b):
    return a+b

#call function and print value
#inside print call the function since function returning that addition value
print(add(1,3))

#default parameter
def greet(name="World"):
    print("Hello", name)

greet() #since function not taking any arguement so its print default name that present in the function
greet("Sanvi")

#Keyword Argument
def greet(name, age):
    print(f'Name:{name}, Age:{age}')
greet(age=25, name="Mangesh")

#Arbitrary Number of Arguments
def sum_number(*args):
    total=0
    for num in args:
        total += num
    return total

result = sum_number(1,2,3,4,5)
print(result)

#Return statement
def multiply(a,b):
    return(a*b)
result = multiply(12,4)
print(result)

#DocString
def greet(name):
    """
    This function greets the user
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    print("Hello",name)

#scope of variable
x = 10
def func():
    y = 20 
    print(x)
    print(y)

func()

#lamda function
square = lambda x:x**2
result = square(5)
print(result,"here is the result of lamda function")

#mini Project Hangman

import random
def choose_word():
    words = ["apple", "banana", "cherry", "oranges", "grapes"]
    return random.choice(words)
print(choose_word())

def display_word(word, guessed_letters):
    result = ""
    for char in word:
        if char in guessed_letters:
            result += char
        else:
            result += "_"
    return result

def hangman():
    print("Hangman Game")
    word = choose_word()
    guessed_letters = []
    attempts =6
    while attempts> 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter:").lower()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("Already guessed that letter")
            elif guess in word:
                guessed_letters.append(guess)
                if display_word(word,guessed_letters) == word:
                    print("Well done")
                    break
            else:
                attempts -= 1
        else:
            print("Invalid single letter")
    else:
        print("You run out of attempts")

hangman()
    