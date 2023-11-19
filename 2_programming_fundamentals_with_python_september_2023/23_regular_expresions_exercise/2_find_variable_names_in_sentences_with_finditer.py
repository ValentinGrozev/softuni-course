import re

variable_names = input()

pattern = r"\b\_([A-Za-z0-9]+)\b"
matches = re.finditer(pattern, variable_names)

list_with_searched_strings = []

for match in matches:
    searched_string = match.group(1)
    list_with_searched_strings.append(searched_string)

print(",".join(list_with_searched_strings))
