needed_money_for_vacation = float(input())
money_on_hand = float(input())

all_money = 0 + money_on_hand
counter = 0
counter_spend = 0

while all_money < needed_money_for_vacation:
    text = input()
    current_money = float(input())
    counter += 1
    if text == "spend":
        counter_spend += 1
        all_money -= current_money
        if all_money < 0:
            all_money = 0
        if counter_spend == 5:
            break

    elif text == "save":
        all_money += current_money
        counter_spend = 0

if counter_spend == 5:
    print("You can't save the money.")
    print(f"{counter}")
else:
    print(f"You saved the money for {counter} days.")