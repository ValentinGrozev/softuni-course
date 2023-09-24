destination = input()
minimal_budget = float(input())

all_saved_money = 0
money = float(input())
flag_break = False

while destination != "End":
    while all_saved_money <= minimal_budget:
        saved_money = float(money)
        all_saved_money += saved_money
        if all_saved_money >= minimal_budget:
            flag_break = True
            all_saved_money = 0
            break

        money = input()

    if flag_break:
        print(f"Going to {destination}!")
        destination = input()
        if destination == "End":
            break
        minimal_budget = float(input())
        money = input()


