budget = float(input())
number_of_statists = int(input())
price_for_clothes = float(input())

price_for_decor = 0.1 * budget

if number_of_statists >= 150:
    price_for_clothes = price_for_clothes * 0.9

total_cost = number_of_statists * price_for_clothes + price_for_decor
diff = abs(total_cost - budget)

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!" )
    print(f"Wingard starts filming with {diff:.2f} leva left.")