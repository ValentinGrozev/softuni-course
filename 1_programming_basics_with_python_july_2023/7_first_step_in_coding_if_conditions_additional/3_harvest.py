from math import floor, ceil

area_vineyard = int(input())
grape_per_square = float(input())
needed_liters_of_wine = int(input())
workers = int(input())

total_grape_in_kg = area_vineyard * grape_per_square
harvest_for_wine = 0.4 * total_grape_in_kg
total_liters_of_wine = harvest_for_wine / 2.5
total_liters_of_wine_floor = floor(total_liters_of_wine)

diff = abs(needed_liters_of_wine - total_liters_of_wine)
diff_floor = floor(diff)
diff_ceil = ceil(diff)
wine_per_workers = ceil(diff_ceil / workers)


if total_liters_of_wine < needed_liters_of_wine:
    print(f"It will be a tough winter! More {diff_floor} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {total_liters_of_wine_floor} liters.")
    print(f"{diff_ceil} liters left -> {wine_per_workers} liters per person.")
