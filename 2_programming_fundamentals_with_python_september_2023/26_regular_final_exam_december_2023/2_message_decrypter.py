import re

number_of_messages = int(input())
valid_messages = []

for current_message in range(number_of_messages):
    message = input()
    pattern = r"^\$[A-Z]{1}[a-z]{2,}\$: \[[0-9]+\]\|\[[0-9]+\]\|\[[0-9]+\]\|$|^\%[A-Z]{1}" \
              r"[a-z]{2,}\%: \[[0-9]+\]\|\[[0-9]+\]\|\[[0-9]+\]\|$"
    match = re.findall(pattern, message)
    if match:
        valid_messages.append(match)
    else:
        valid_messages.append("False")

for current_valid_message in valid_messages:
    if current_valid_message == "False":
        print("Valid message not found!")
    elif "$" in current_valid_message[0]:
        pattern = r"^\$([A-Z]{1}[a-z]{2,})\$: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$"
        match = re.finditer(pattern, current_valid_message[0])
        for current_match in match:
            tag = current_match.group(1)
            first_group = int(current_match.group(2))
            second_group = int(current_match.group(3))
            third_group = int(current_match.group(4))
            print(f"{tag}: {chr(first_group)}{chr(second_group)}{chr(third_group)}")
    elif "%" in current_valid_message[0]:
        pattern = r"^\%([A-Z]{1}[a-z]{2,})\%: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$"
        match = re.finditer(pattern, current_valid_message[0])
        for current_match in match:
            tag = current_match.group(1)
            first_group = int(current_match.group(2))
            second_group = int(current_match.group(3))
            third_group = int(current_match.group(4))
            print(f"{tag}: {chr(first_group)}{chr(second_group)}{chr(third_group)}")
