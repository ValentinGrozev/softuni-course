fuel_type = str(input())
amount_of_fuel = float(input())
club_card = str(input())

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

x = "Gasoline"
y = "Diesel"
z = "Gas"
k = "Yes"
W = "No"

if fuel_type == x:
    gasoline = gasoline_price - 0.18
    price = amount_of_fuel * (gasoline if club_card == k else gasoline_price)
elif fuel_type == y:
    diesel = diesel_price - 0.12
    price = amount_of_fuel * (diesel if club_card == k else diesel_price)
elif fuel_type == z:
    gas = gas_price - 0.08
    price = amount_of_fuel * (gas if club_card == k else gas_price)
else:
    raise Exception('Incorrect data')

if 20 <= amount_of_fuel <= 25:
    price = price * 0.92
    print(f"{price:.2f} lv.")
elif amount_of_fuel > 25:
    price = price * 0.90
    print(f"{price:.2f} lv.")
else:
    print(f"{price:.2f} lv.")
