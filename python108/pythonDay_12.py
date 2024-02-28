#Day 12 python List comprehensions
#List comprehensions provide a more compact and readable syntax compared to traditional for loops.

squares = []
for x in range(1,6):
    squares.append(x**2)

print(squares,"output from tranditional loop")

#List comprehension
squares2 = [x**2 for x in range(1,6)]
print(squares2, "using list comprehension")

