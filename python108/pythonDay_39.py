x = -5
if x < 0:
    raise ValueError("x cannot be negative")


#Custom Exception Classes
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


def divide(x,y):
    if y ==0:
        raise CustomError("Division by zero is not allowed")
    return x/y

try:
    result = divide(10,0)
    print(result)

except CustomError as e:
    print("Error:",e)