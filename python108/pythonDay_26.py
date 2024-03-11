file = open("D:\pythonDSA\PythonDSA\python108\example.txt","r") # open file in read mode

file1 = open("D:\pythonDSA\PythonDSA\python108\example.txt", "w") #open file in write mode

file3 = open("D:\pythonDSA\PythonDSA\python108\example.txt", "a") #open file in append mode


content = file.read()
print(content)

line = file.readline()
# print(line)


#writing file
file1.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

#closing the file
file.close()

#example
file1.write("Hello world\n")
file1.write("This is a new line \n")
file.close()

file = open("D:\pythonDSA\PythonDSA\python108\example.txt")
content = file.read()
print(content)
file.close()

#using with 
with open("D:\pythonDSA\PythonDSA\python108\example.txt","r") as file:
    content = file.read()
    print(content)
