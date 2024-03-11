# 27 Day : File handling best practices and error handling
with open("D:\pythonDSA\PythonDSA\python108\example.txt","r") as file:
    content = file.read()
    print(content)

#check file is present or not
import os

if os.path.exists("D:\pythonDSA\PythonDSA\python108\example.txt"):
    with open("D:\pythonDSA\PythonDSA\python108\example.txt","r") as file:
        content1 = file.read()
        print(content1)
else:
    print("File doesnot exist in the provided path")


#using try except block for error handling
try:
    with open("D:\pythonDSA\PythonDSA\python108\example.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("permission denied")
except IOError:
    print("error occured while reading the file")
    