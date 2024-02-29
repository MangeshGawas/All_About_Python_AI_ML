# Day 14: Practice Writing Functions and Loops

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

#prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(0**0.5) + 1):
        if n % i == 0:
            return False
        return True
print(is_prime(11))