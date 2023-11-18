import re

phone_numbers_to_check = input()

pattern = r"(\+359)([\s|-])(2{1})\2([0-9]{3})\2([0-9]{4})\b"
matches = re.finditer(pattern, phone_numbers_to_check)

list_with_valid_numbers = []

for element in matches:
    first_part = element.group(1)
    second_part = element.group(2)
    third_part = element.group(3)
    fourth_part = element.group(4)
    fifth_part = element.group(5)
    final_number = first_part+second_part+third_part+second_part+fourth_part+second_part+fifth_part
    list_with_valid_numbers.append(final_number)

print(", ".join(list_with_valid_numbers))