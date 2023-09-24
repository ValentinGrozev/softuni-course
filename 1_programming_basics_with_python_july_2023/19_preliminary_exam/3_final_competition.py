number_of_dancers = int(input())
number_of_points = float(input())
season = input()
place = input()

if place == "Bulgaria":
    earn_money = number_of_dancers * number_of_points
    if season == "summer":
        expenses = 0.05
        earn_money_after_expenses = earn_money * (1 - expenses)
    elif season == "winter":
        expenses = 0.08
        earn_money_after_expenses = earn_money * (1 - expenses)
elif place == "Abroad":
    earn_money = (number_of_dancers * number_of_points) * 1.5
    if season == "summer":
        expenses = 0.10
        earn_money_after_expenses = earn_money * (1 - expenses)
    elif season == "winter":
        expenses = 0.15
        earn_money_after_expenses = earn_money * (1 - expenses)

money_donated = earn_money_after_expenses * 0.75
money_left = earn_money_after_expenses - money_donated
money_per_one_dancer = money_left / number_of_dancers

print(f"Charity - {money_donated:.2f}")
print(f"Money per dancer - {money_per_one_dancer:.2f}")
