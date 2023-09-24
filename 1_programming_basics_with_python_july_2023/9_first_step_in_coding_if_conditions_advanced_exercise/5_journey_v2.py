budget = float(input())
seasons = input()

cost = 0
vacation = ""
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if seasons == "summer":
        vacation = "Camp"
        cost = 0.3 * budget
    elif seasons == "winter":
        vacation = "Hotel"
        cost = 0.7 * budget

elif budget <= 1000:
    destination = "Balkans"
    if seasons == "summer":
        vacation = "Camp"
        cost = 0.4 * budget
    elif seasons == "winter":
        vacation = "Hotel"
        cost = 0.8 * budget

elif budget > 1000:
    destination = "Europe"
    vacation = "Hotel"
    cost = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{vacation} - {cost:.2f}")