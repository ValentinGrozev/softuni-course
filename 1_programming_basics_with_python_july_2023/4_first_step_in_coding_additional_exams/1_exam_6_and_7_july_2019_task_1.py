from math import ceil

people_count = int(input())
tax_paid = float(input())
price_for_sun_lounger = float(input())
price_for_umbrella = float(input())

needed_sun_lounger = ceil(0.75 * people_count)
needed_umbrella = ceil(0.5 * people_count)

all_cost = people_count * tax_paid + price_for_sun_lounger * needed_sun_lounger + price_for_umbrella * needed_umbrella
print(f"{all_cost:.2f}", "lv.")