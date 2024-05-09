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