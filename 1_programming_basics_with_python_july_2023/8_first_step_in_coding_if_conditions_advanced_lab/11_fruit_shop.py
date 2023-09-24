fruit = input()
day_of_week = input()
quantity = float(input())

total_price = 0
if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    if fruit == "banana":
        total_price = quantity * 2.50
        print(f"{total_price:.2f}")
    elif fruit == "apple":
        total_price = quantity * 1.20
        print(f"{total_price:.2f}")
    elif fruit == "orange":
        total_price = quantity * 0.85
        print(f"{total_price:.2f}")
    elif fruit == "grapefruit":
        total_price = quantity * 1.45
        print(f"{total_price:.2f}")
    elif fruit == "kiwi":
        total_price = quantity * 2.70
        print(f"{total_price:.2f}")
    elif fruit == "pineapple":
        total_price = quantity * 5.50
        print(f"{total_price:.2f}")
    elif fruit == "grapes":
        total_price = quantity * 3.85
        print(f"{total_price:.2f}")
    else:
        print("error")
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        total_price = quantity * 2.70
        print(f"{total_price:.2f}")
    elif fruit == "apple":
        total_price = quantity * 1.25
        print(f"{total_price:.2f}")
    elif fruit == "orange":
        total_price = quantity * 0.90
        print(f"{total_price:.2f}")
    elif fruit == "grapefruit":
        total_price = quantity * 1.60
        print(f"{total_price:.2f}")
    elif fruit == "kiwi":
        total_price = quantity * 3.00
        print(f"{total_price:.2f}")
    elif fruit == "pineapple":
        total_price = quantity * 5.60
        print(f"{total_price:.2f}")
    elif fruit == "grapes":
        total_price = quantity * 4.20
        print(f"{total_price:.2f}")
    else:
        print("error")
else:
    print("error")