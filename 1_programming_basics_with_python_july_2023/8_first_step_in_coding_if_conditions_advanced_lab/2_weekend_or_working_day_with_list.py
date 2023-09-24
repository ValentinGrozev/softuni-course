day_in_text = input()

days_1 = {"Monday","Tuesday","Wednesday","Thursday","Friday"}
days_2 = {"Saturday","Sunday"}

if day_in_text in days_1:
    print("Working day")
elif day_in_text in days_2:
    print("Weekend")
else:
    print("Error")