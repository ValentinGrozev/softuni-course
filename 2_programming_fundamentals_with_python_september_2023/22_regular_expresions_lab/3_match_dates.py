import re

dates_to_check = input()
pattern = r"(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})"

matches = re.finditer(pattern, dates_to_check)

for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")
