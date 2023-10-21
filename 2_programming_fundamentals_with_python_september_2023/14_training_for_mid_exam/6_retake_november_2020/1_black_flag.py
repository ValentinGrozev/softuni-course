days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

total_plunder_gained = 0

for day in range(1, days_of_plunder + 1):
    total_plunder_gained += daily_plunder
    if day % 3 == 0:
        total_plunder_gained += 0.5 * daily_plunder
    if day % 5 == 0:
        total_plunder_gained = 0.7 * total_plunder_gained

if total_plunder_gained >= expected_plunder:
    print(f"Ahoy! {total_plunder_gained:.2f} plunder gained.")
else:
    percentage = (total_plunder_gained / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
