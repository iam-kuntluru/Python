import re

text = "Python is a dynamic language"
pattern = r"dynamic"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
