hour_of_exam = int(input())
minute_of_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

all_exam_minutes = (hour_of_exam * 60) + minute_of_exam
all_arrival_minutes = (arrival_hour * 60) + arrival_minute
diff = abs(all_exam_minutes - all_arrival_minutes)
hour = ""
minute = ""

if all_exam_minutes < all_arrival_minutes:
    print("Late")
    if diff >= 60:
        hour = diff // 60
        minute = diff % 60
        print(f"{hour}:{minute:02d} hours after the start")
    else:
        minute = diff % 60
        print(f"{diff} minutes after the start")
elif all_exam_minutes >= all_arrival_minutes:
    if 0 < diff <= 30:
        print("On Time")
        print(f"{diff} minutes before the start")
    elif diff == 0:
        print("On Time")
    elif 30 < diff < 60:
        print("Early")
        print(f"{diff} minutes before the start")
    else:
        print("Early")
        hour = diff // 60
        minute = diff % 60
        print(f"{hour}:{minute:02d} hours before the start")
