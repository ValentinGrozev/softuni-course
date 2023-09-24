from math import ceil, floor

days_leave = int(input())
all_food_in_kg = int(input())
food_for_dog_per_day = float(input())
food_for_cat_per_day = float(input())
food_for_turtle_per_day = float(input())

needed_fodf_for_dog = days_leave * food_for_dog_per_day
needed_food_for_cat = days_leave * food_for_cat_per_day
needed_food_for_turtle = (days_leave * food_for_turtle_per_day) / 1000

all_needed_food = needed_fodf_for_dog + needed_food_for_cat + needed_food_for_turtle
diff = abs(all_food_in_kg - all_needed_food)
diff_ceil = ceil(diff)
diff_floor = floor(diff)

if all_food_in_kg >= all_needed_food:
    print(f"{diff_floor} kilos of food left")
else:
    print(f"{diff_ceil} more kilos of food are needed.")