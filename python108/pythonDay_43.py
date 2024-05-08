#regular expression
import re 
pattern = r'apple'
text = 'I love apples'

match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("pattern not found")

match_starting = re.match(pattern,text)
if match:
    print("pattern found at the start:", match.group())
else:
    print("Match not found")


#find all occurance in the string
text = "I love apples, apples are tasty"
matches = re.findall(pattern, text)
print("Occurances:",matches)

#replace a pattern with a replacement
new_text = re.sub(pattern, "banana", text)
print("New text:",new_text)
