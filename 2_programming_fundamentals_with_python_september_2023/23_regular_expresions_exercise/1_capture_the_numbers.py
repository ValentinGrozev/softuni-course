import re

text = input()

while True:
    pattern = r"\d+"
    matches = re.findall(pattern, text)
    if matches:
        print(" ".join(matches), end=" ")

    text = input()
