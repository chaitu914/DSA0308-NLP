import re

text = input("Enter a sentence: ")
pattern = input("Enter the word to search: ")

match = re.search(pattern, text)

if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found.")