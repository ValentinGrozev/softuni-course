day_in_text = input()

if day_in_text == "Monday" or day_in_text == "Tuesday" or day_in_text == "Wednesday" or day_in_text == "Thursday" or day_in_text == "Friday":
    print("Working day")
elif day_in_text == "Saturday" or day_in_text == "Sunday":
    print("Weekend")
else:
    print("Error")
