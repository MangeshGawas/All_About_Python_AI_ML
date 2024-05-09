import numpy as np 
arr =  np.array([1,2,3,4,5])
print(arr)
print(type(arr))

arr_2 = np.array([[1,2,3],[4,5,6]])
print(arr_2)

#create Zeros
zeros = np.zeros((2,3))
print(zeros)

#creates ones
ones = np.ones((2,3))
print(ones)

#create a numpy array with a range ofvalues
print("__________________________")
range_arr = np.arange(1,10,3)
print(range_arr)

#create a numpy array with evenly
print("__________________________")

linspace_arr = np.linspace(0,1,5)
print(linspace_arr)

print("Numpy Operation")

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

print("____________________")
print("Dot Product")
dot_product = np.dot(arr1,arr2)
print(dot_product)

print("____________________")
arr = np.array([[1,2],[3,4]])
print(arr.T)


#numpy functions
arr = np.array([1,2,3,4,5])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))