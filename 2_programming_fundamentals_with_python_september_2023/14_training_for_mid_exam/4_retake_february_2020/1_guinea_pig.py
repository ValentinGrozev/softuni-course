quantity_of_food_in_kg = float(input())
quantity_of_hay_in_kg = float(input())
quantity_of_cover_in_kg = float(input())
guineas_pig_weight_in_kg = float(input())

days_per_month = 30

quantity_of_food_in_gram = 1000 * quantity_of_food_in_kg
quantity_of_hay_in_gram = 1000 * quantity_of_hay_in_kg
quantity_of_cover_in_gram = 1000 * quantity_of_cover_in_kg

for day in range(1, days_per_month + 1):
    quantity_of_food_in_gram -= 300
    if day % 2 == 0:
        quantity_of_hay_in_gram -= quantity_of_food_in_gram * 0.05
    if day % 3 == 0:
        quantity_of_cover_in_gram -= (guineas_pig_weight_in_kg * 1000) / 3

if quantity_of_food_in_gram > 0 and quantity_of_hay_in_gram > 0 and quantity_of_cover_in_gram > 0:
    print(f"Everything is fine! Puppy is happy! Food: {(quantity_of_food_in_gram / 1000):.2f}, "
          f"Hay: {(quantity_of_hay_in_gram / 1000):.2f}, Cover: {(quantity_of_cover_in_gram / 1000):.2f}.")
else:
    print("Merry must go to the pet store!")
