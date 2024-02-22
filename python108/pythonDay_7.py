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
