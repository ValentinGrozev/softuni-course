hours = int(input())
minutes = int(input())

total_time = hours * 60 + minutes + 15
total_hours = total_time // 60
total_mins = total_time % 60

if total_hours > 23:
    total_hours = 0

if total_mins < 10:
    print(f"{total_hours}:0{total_mins}")
else:
    print(f"{total_hours}:{total_mins}")