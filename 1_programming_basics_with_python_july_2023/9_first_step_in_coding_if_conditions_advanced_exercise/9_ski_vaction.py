days = int(input())
type_of_room = input()
assessment = input()

nights = days - 1
cost = 0

if type_of_room == "apartment":
    if days < 10:
        cost = nights * 25
        cost = cost * 0.70
        if assessment == "positive":
            cost = cost * 1.25
            print(f"{cost:.2f}")
        elif assessment == "negative":
            cost = cost * 0.9
            print(f"{cost:.2f}")
    if 15 >= days >= 10:
        cost = nights * 25
        cost = cost * 0.65
        if assessment == "positive":
            cost = cost * 1.25
            print(f"{cost:.2f}")
        elif assessment == "negative":
            cost = cost * 0.9
            print(f"{cost:.2f}")
    if 15 < days:
        cost = nights * 25
        cost = cost * 0.50
        if assessment == "positive":
            cost = cost * 1.25
            print(f"{cost:.2f}")
        elif assessment == "negative":
            cost = cost * 0.9
            print(f"{cost:.2f}")
if type_of_room == "president apartment":
    if days < 10:
        cost = nights * 35
        cost = cost * 0.90
        if assessment == "positive":
            cost = cost * 1.25
            print(f"{cost:.2f}")
        elif assessment == "negative":
            cost = cost * 0.9
            print(f"{cost:.2f}")
    if 15 >= days >= 10:
        cost = nights * 35
        cost = cost * 0.85
        if assessment == "positive":
            cost = cost * 1.25
            print(f"{cost:.2f}")
        elif assessment == "negative":
            cost = cost * 0.90
            print(f"{cost:.2f}")
    if 15 < days:
        cost = nights * 35
        cost = cost * 0.80
        if assessment == "positive":
            cost = cost * 1.25
            print(f"{cost:.2f}")
        elif assessment == "negative":
            cost = cost * 0.90
            print(f"{cost:.2f}")
if type_of_room == "room for one person":
    cost = nights * 18
    if assessment == "positive":
        cost = cost * 1.25
        print(f"{cost:.2f}")
    elif assessment == "negative":
        cost = cost * 0.90
        print(f"{cost:.2f}")
