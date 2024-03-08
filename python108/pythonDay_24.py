#Day 24 : String Manipulation - slicing, concatenation and formatting
s = "Hello , World"
substring = s[3:8]
print(substring)

#concatenating String
s1 = "Hello"
s2 = "world"
concatenated_string = s1+ "," + s2 +"!"
print(concatenated_string)

#join

word = ["Hello","world"]
concatenated_string = " ".join(word)
print(concatenated_string)

#string formatting
name = "Jerry"
age = 30
print(f"{name} is a mouse in cartoon and his is {age} old")