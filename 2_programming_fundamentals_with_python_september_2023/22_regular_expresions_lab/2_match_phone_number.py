import re

phone_numbers_to_check = input()

pattern = r"\+359\s[2]{1}\s[0-9]{3}\s[0-9]{4}|\+359\-[2]{1}\-[0-9]{3}\-[0-9]{4}\b"
matches = re.findall(pattern, phone_numbers_to_check)

print(", ".join(matches))
