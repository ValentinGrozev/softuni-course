number_of_days = int(input())
number_of_hours = int(input())

day_sum = 0
total_sum = 0

for day in range(1, number_of_days + 1):
    for hour in range(1, number_of_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            day_sum += 2.50
            total_sum += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            day_sum += 1.25
            total_sum += 1.25
        else:
            day_sum += 1
            total_sum += 1
    print(f"Day: {day} - {day_sum:.2f} leva")
    day_sum = 0
print(f"Total: {total_sum:.2f} leva")






