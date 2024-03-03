#Day19
my_dict = {
    'apple':10,
    'banana':5,
    'orange':8
}

mixed_dict = {
    'name':"Tom",
    'age': 29,
    'is_cartoon':True
}

#accessing Element
print(my_dict['apple'])
print(my_dict['orange'])

print(my_dict.get('banana'))
print(my_dict.get('grapes'))

#dictionary Method
keyOfDictionary = my_dict.keys()
print(keyOfDictionary)
valueOfDictionary = my_dict.values()
print(valueOfDictionary)

itemsOfDictionary = my_dict.items()
print(itemsOfDictionary)

#update
my_dict.update({
    'grapes':12,
    'banana':7
})

print(my_dict,"here is the updated dictionary")

