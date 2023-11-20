import re

links_to_check = input()
pattern = r"(([w]{3}\.)([a-zA-Z0-9\-]+)(\.[a-z]+)+)"

while links_to_check:
    matches = re.findall(pattern, links_to_check)
    if matches:
        for match in matches:
            valid_email = match[0]
            print(valid_email)

    links_to_check = input()
