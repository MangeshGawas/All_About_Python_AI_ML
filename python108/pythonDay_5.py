#Lets begin the python day 5 : Python Loop

#Python basically have 2 types of loop ie for and while loop

#for Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#while Loop
#loop beginning with 0 because i = 0 , ie like initializing the 
i = 0
while i <= 5:
    print(i)
    i = i+1

#Logic Building code
#1) Sum of number
total = 0
for num in range(1,11):
    total += num
print("Sum if the 1 to 10 :",total)

#2)Multiplication Table
num = int(input("which table you want , please mentioned the number"))
print("Multiplication table of ", num)
for i in range(1,11):
    print(num, "x", i, "=", num * i)

#3)Factorial Calculation
num = 5
factorial = 1
for i in range(1, num+1):
    factorial *= i
print("Factorial of ", num ,":", factorial)

#mini Project
#Simple calculator code

def calculator():
    print("Welcome to the Simple Calculator")
    while True:
        print("\nOperation")
        print("1. Addition")
        print("2. Subbtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter your choice (1-5)")
        if choice == "5":
            print("Existing the calculator")
            break
        elif choice in ("1",'2','3','4'):
            num1 = float(input("Enter the first number"))
            num2 = float(input("Enter the second number"))
            if choice == "1":
                result = num1 + num2
                print("Result:",result)
            elif choice == "2":
                result = num1 - num2
                print("Result:",result)
            elif choice == "3":
                result = num1 * num2
                print("Result:",result)
            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print("Result:",result)
                else:
                    print("Error, Division by zero")
        else:
            print("Invalid Choice")
calculator()