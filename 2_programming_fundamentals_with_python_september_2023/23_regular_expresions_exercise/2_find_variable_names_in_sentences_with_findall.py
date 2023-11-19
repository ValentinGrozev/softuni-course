import re

variable_names = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, variable_names)
print(",".join(matches))
