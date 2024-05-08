#regular expression
import re 
pattern = r'apple'
text = 'I love apples'

match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("pattern not found")

