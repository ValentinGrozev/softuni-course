budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())

x = nights
y = price_per_night

if x > 7:
    y = y * 0.95
else:
    y = y

nights_cost = x * y
additional_cost = budget * (percent_additional_costs/100)
all_cost = nights_cost + additional_cost

if budget >= all_cost:
    print(f"Ivanovi will be left with {budget-all_cost:.2f} leva after vacation.")
else:
    print(f"{abs(budget-all_cost):.2f} leva needed.")