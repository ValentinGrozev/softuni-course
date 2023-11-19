import re

text = input().lower()
word_to_check = input().lower()
pattern = fr"\b{word_to_check}\b"

matches = re.findall(pattern, text)

print(len(matches))
