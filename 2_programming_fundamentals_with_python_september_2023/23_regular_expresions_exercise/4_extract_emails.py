import re

e_mail_address_to_validate = input()

pattern = r"\s(([a-z0-9]+[\-\.\_a-z0-9]*)@([a-z\-]+)(\.[a-z]+)+)\b"
matches = re.finditer(pattern, e_mail_address_to_validate)

for match in matches:
    valid_email = match.group(1)
    print(valid_email)
