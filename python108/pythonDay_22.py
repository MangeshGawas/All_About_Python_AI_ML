# day-22: Nested Data structure
# lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][0] ) #[row][col]

#dictionaries
student_records ={
    'Alice':{'age':25, 'major':'computer science'},
    'Bob':{'age':22, 'major':'Engineering'}
}

print(student_records['Alice']['age'])
print(student_records['Bob']['major'])

#Mixed nested data structure
students = [
    {'name':"Alice",'age':25},
    {'name':'Bob','age':22}
]
print(students[0]['name'])

grades = {
    'Alice': [90, 85, 88],
    'Bob': [85, 80, 82]
}

print(grades['Bob'][1])