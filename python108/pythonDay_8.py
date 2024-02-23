#Day 9 : Dictionaries , nesting and the secret Auction

#create Dictionaries {}
person = {"name":"Alice","age":30, "city":"new york"}

print(person["name"])

#adding and modifying elements
person["email"] = "alice@gmail.com"
person["age"] = 31

'''Dictionary Methods: Python provides various built-in methods to manipulate dictionaries, such as 
keys(), values(), items(), pop(), popitem(), clear(), update(), etc.
'''

#dictionary methods
print(person.keys())
print(person.values())


#Nested Lists
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][1]) 


#nested dictionaries
person ={
    "name":"Mangesh",
    "age":25,
    "address":{
        "city":"New York",
        "zipcode":"10001"
    }
}

print(person["address"]["city"])

#Scret_aution is pending due to lack of understanding of rules