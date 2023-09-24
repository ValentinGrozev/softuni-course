day_of_week = input()

ticket_price_1 = 12
ticket_price_2 = 14
ticket_price_3 = 16

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday":
    print(ticket_price_1)
elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    print(ticket_price_2)
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    print(ticket_price_3)