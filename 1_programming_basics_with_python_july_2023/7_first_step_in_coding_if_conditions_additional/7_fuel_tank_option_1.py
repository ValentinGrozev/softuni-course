fuel_type = str(input())

v = "Diesel"
b = "Gasoline"
c = "Gas"

if fuel_type == v:
    liters_in_tank = float(input())
    if liters_in_tank >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
elif fuel_type == b:
    liters_in_tanks = float(input())
    if liters_in_tanks >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
elif fuel_type == c:
    liters_in_tank = float(input())
    if liters_in_tank >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")