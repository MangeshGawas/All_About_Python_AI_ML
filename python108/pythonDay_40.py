def apply_operation(func,x,y):
    return func(x,y)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

result1 = apply_operation(add,3,5)
result2 = apply_operation(subtract, 7,5)

print(f"result1 ={result1}\nresult2={result2}")


######Lamda Expression

add1 = lambda x,y:x+y
result = add1(99,1)
print("result =",result)


