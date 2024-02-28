#day 10 is Recurssion
#Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(4)
print(result)

#fibonacci
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(7))

#binary search
def binary_search(arr, target, low , high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, high)
    else:
        return binary_search(arr, target, low, mid-1)
    

arr = [1,2,3,4,5,6,7,8]
print(binary_search(arr, 5,0,len(arr)-1))





