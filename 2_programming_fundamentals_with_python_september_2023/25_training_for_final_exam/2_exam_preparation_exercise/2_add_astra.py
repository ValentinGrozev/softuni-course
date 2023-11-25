import re

food_information = input()
pattern = r"([#|])([A-Za-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)([\d]+)(\1)"
matches = re.findall(pattern, food_information)

total_calories = 0

for match in matches:
    calories = match[5]
    total_calories += int(calories)

days_to_live = total_calories // 2000
print(f"You have food to last you for: {days_to_live} days!")

for match in matches:
    food_name = match[1]
    expiration_date = match[3]
    calories = match[5]
    print(f"Item: {food_name}, Best before: {expiration_date}, Nutrition: {calories}")
