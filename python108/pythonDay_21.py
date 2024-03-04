#day21 iterating over dictionaries
student_score = {'alice':85,
                 'Bob':90,
                 "Charlie":75}


#iterate over keys
for student in student_score:
    print(student)

#iterate over values
for score in student_score.values():
    print(score)

#iterate over key - Value pair
for student , score in student_score.items():
    print(student,":",score)

#Dictionary comprehension
squared_values = {x:x**2 for x in range(1,6)}
print(squared_values)

even_squared = {x: x**2 for x in range(1,11) if x%2==0}
print(even_squared)