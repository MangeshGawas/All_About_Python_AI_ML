#Python Day 9

def greet(name,age):
    print("Hello,", name, "you are",age, "year old")

greet("Tom",21)


#Gobal Scope
x = 10
def func():
    print(x)
func()

def func2():
    global x
    x = 20 #modifying global variable

func2()
print(x , "after modifying")

####Local Variable
def funcLocalVariable():
    y = 20
    print(y, "here is the y")
funcLocalVariable()

#if I need print y outside the funcLocalVarible it will throw an error


#Variable scope resolutions
def outer():
    y = 20

    def inner():
        print(x , "inner")
        print(y, 'inner') #accessing enclosing functions local vaeiable
    inner()
outer()

#NON local
def outer1():
    y = 20

    def inner():
        nonlocal y
        y =400
        print(x , "inner")
        print(y, 'inner non local') #accessing enclosing functions local vaeiable
    inner()
outer1()