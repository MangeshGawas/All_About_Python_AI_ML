#Lets begins with the day 3
#Control flow, logical operator and mini Project /project

#Control Flow statement if, if else, if elif else

#if
x = 5
if x > 0:
    print('x is positive')


#if else
y = -3
if y >=0:
    print('y is non negative')
else:
    print("y is negative")

#if elif else
z = 0
if  z < 0:
    print("z is negative number")
elif z > 0:
    print('z is positive number')
else:
    print('z is 0')


#Logical Opertor
a = 10
b = 5

if a > 0 and b>0:
    print(f"Both {a} and {b} are positive number")

if a > 0 or b>0:
    print(f"Both {a} or {b} are positive number")

if not(a<0):
    print("At least one of a or b is positive")

#mini project : odd-even Number checker

#take a user input for a number
num = int(input("Enter the number which you want to check is even or odd"))

#check if the number is odd or even

if num % 2 == 0:
    print(f"{num}Provided number is Even")
else:
    print("Its Odd number")
