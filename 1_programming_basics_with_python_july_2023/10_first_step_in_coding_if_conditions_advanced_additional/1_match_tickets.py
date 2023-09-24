budget = float(input())
category_ticket = input()
number_people_in_group = int(input())

transport_cost = 0

if 1 <= number_people_in_group <= 4:
    transport_cost = budget * 0.75
    budget_left = budget - transport_cost
    if category_ticket == "VIP":
        needed_money = number_people_in_group * 499.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif category_ticket == "Normal":
        needed_money = number_people_in_group * 249.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
elif 5 <= number_people_in_group <= 9:
    transport_cost = budget * 0.60
    budget_left = budget - transport_cost
    if category_ticket == "VIP":
        needed_money = number_people_in_group * 499.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif category_ticket == "Normal":
        needed_money = number_people_in_group * 249.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
elif 10 <= number_people_in_group <= 24:
    transport_cost = budget * 0.50
    budget_left = budget - transport_cost
    if category_ticket == "VIP":
        needed_money = number_people_in_group * 499.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif category_ticket == "Normal":
        needed_money = number_people_in_group * 249.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
elif 25 <= number_people_in_group <= 49:
    transport_cost = budget * 0.40
    budget_left = budget - transport_cost
    if category_ticket == "VIP":
        needed_money = number_people_in_group * 499.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif category_ticket == "Normal":
        needed_money = number_people_in_group * 249.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
else:
    transport_cost = budget * 0.25
    budget_left = budget - transport_cost
    if category_ticket == "VIP":
        needed_money = number_people_in_group * 499.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif category_ticket == "Normal":
        needed_money = number_people_in_group * 249.99
        diff = abs(budget_left - needed_money)
        if budget_left >= needed_money:
            print(f"Yes! You have {diff:.2f} leva left.")
        else:
            print(f"Not enough money! You need {diff:.2f} leva.")
