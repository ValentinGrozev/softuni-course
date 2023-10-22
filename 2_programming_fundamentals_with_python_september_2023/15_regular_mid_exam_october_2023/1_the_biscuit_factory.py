from math import floor

number_of_biscuits_per_worker_per_day = int(input())
count_of_the_workers = int(input())
number_of_biscuits_to_compare_with_other_factory = int(input())

produced_biscuits = 0
days_in_month = 30

for day in range(1, days_in_month + 1):
    if day % 3 == 0:
        produced_biscuits += int(floor(0.75 * (number_of_biscuits_per_worker_per_day * count_of_the_workers)))
    else:
        produced_biscuits += int(floor(number_of_biscuits_per_worker_per_day * count_of_the_workers))

biscuit_difference = abs(produced_biscuits - number_of_biscuits_to_compare_with_other_factory)
percentage = (biscuit_difference / number_of_biscuits_to_compare_with_other_factory) * 100

print(f"You have produced {produced_biscuits} biscuits for the past month.")
if produced_biscuits > number_of_biscuits_to_compare_with_other_factory:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
