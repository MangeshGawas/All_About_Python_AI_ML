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
