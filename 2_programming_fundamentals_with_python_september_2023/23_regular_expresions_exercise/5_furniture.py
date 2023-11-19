import re

purchase = input()

furniture_list = []
total_cost = 0

while purchase != "Purchase":
    pattern = r">>([A-Za-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)"
    matches = re.finditer(pattern, purchase)
    for match in matches:
        furniture = match.group(1)
        price = match.group(2)
        quantity = match.group(3)
        furniture_list.append(furniture)
        total_cost += float(price) * int(quantity)

    purchase = input()

print("Bought furniture:")
for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
