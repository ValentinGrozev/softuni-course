budget = float(input())
seasons = input()

cost = 0
vacation = ""
destination = ""

if budget <= 100:
    destination = "Bulgaria"
elif budget <= 1000:
    destination = "Balkans"
elif budget >= 1000:
    destination = "Europe"
print(f"Somewhere in {destination}")

if budget <= 100:
    if seasons == "summer":
        vacation = "Camp"
        cost = 0.3 * budget
    elif seasons == "winter":
        vacation = "Hotel"
        cost = 0.7 * budget
    print(f"{vacation} - {cost:.2f}")
elif budget <= 1000:
    if seasons == "summer":
        vacation = "Camp"
        cost = 0.4 * budget
    elif seasons == "winter":
        vacation = "Hotel"
        cost = 0.8 * budget
    print(f"{vacation} - {cost:.2f}")

elif budget > 1000:
    vacation = "Hotel"
    cost = 0.9 * budget
    print(f"{vacation} - {cost:.2f}")

