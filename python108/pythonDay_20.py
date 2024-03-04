# Day 20: Dictionary Manipulation - Adding, Removing, and Modifying Key-Value Pairs
my_dict = {'apple':10, 'banana':5}

#adding a new key value pair
my_dict['orange'] = 8

#using update() method to add multiple key value pairs
my_dict.update({'grapes':12, 'pineapple':15})

print(my_dict)


#removing key value pair
#del or pop()
del my_dict['banana']

orange_value = my_dict.pop('orange')
print(my_dict)
print("Value of 'orange'" , orange_value)