aim_for_the_day = int(input())

service = input()
money_earn = 0
break_flag = False

while service != "closed":
    if service == "haircut":
        type_of_service = input()
        if type_of_service == "mens":
            money_earn += 15
        elif type_of_service == "ladies":
            money_earn += 20
        elif type_of_service == "kids":
            money_earn += 10
    elif service == "color":
        type_of_service = input()
        if type_of_service == "touch up":
            money_earn += 20
        elif type_of_service == "full color":
            money_earn += 30

    if money_earn >= aim_for_the_day:
        break_flag = True
        break

    service = input()

if break_flag:
    print("You have reached your target for the day!")
    print(f"Earned money: {money_earn}lv.")
else:
    diff = abs(money_earn - aim_for_the_day)
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {money_earn}lv.")