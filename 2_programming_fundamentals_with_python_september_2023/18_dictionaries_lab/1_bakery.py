food_and_quantities = input().split()
bakery = {}

for element in range(0, len(food_and_quantities), 2):
    key = food_and_quantities[element]
    value = food_and_quantities[element + 1]
    bakery[key] = int(value)
print(bakery)
