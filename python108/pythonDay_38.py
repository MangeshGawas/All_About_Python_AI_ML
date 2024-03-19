print("try except")
try:
    x = 10/0
except ZeroDivisionError:
    print("Error:Division")


#Handling multiple exception 
print("Handling Multiple exception")
try:
    x = int("abc")
except ValueError:
    print("Error: Invalid conversion to int")
except ZeroDivisionError:
    print("Error: Division by Zero")

#Handling any exception
print("Handling any exception")
try:
    x = 10/0
except Exception as e:
    print("An error is ",e)

#Finally Block
print("Finally Block")
try: 
    x = 10/0
except ZeroDivisionError:
    print("Error:Division by zero")
finally:
    print("Clean up")


print("Else block")
try:
    x= 10/10
except ZeroDivisionError:
    print("error:division by zero")
else:
    print("No error")