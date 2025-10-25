import re

text = "Python is dynamic language"
pattern = r"Python"

match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")
