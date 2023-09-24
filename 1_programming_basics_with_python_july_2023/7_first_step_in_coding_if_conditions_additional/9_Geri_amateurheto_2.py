fuel_type = str(input())
amount_of_fuel = float(input())
club_card = str(input())

prices = {"Gasoline":  2.22, "Diesel": 2.33, "Gas": 0.93}
discounts = {"Gasoline":  0.18, "Diesel": 0.12, "Gas": 0.08}

if club_card == "Yes":
    with_discount = prices[fuel_type] - discounts[fuel_type]
    price = amount_of_fuel * with_discount
elif club_card == "No":
    price = amount_of_fuel * prices[fuel_type]
else:
    raise Exception('Incorrect data')

if 20 <= amount_of_fuel <= 25:
    price = price * 0.92
elif amount_of_fuel > 25:
    price = price * 0.90
print(f"{price:.2f} lv.")
