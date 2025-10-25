import re

text = "Python is a dynamic language"
pattern = r"dynamic"

replacement = "simple, yet"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
