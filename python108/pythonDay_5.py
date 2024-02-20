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
