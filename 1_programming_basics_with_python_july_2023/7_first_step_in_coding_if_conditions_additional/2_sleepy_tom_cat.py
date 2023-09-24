numbers_of_days_off = int(input())

days = 365
play_time_after_work_in_mins = 63
play_time_days_off_in_mins = 127
time_needed = 30000

number_of_work_days = days - numbers_of_days_off
play_time_after_work = number_of_work_days * play_time_after_work_in_mins
play_time_days_off = numbers_of_days_off * play_time_days_off_in_mins

all_play_time = play_time_after_work + play_time_days_off
left_time = abs(time_needed - all_play_time)
all_play_time_hours = left_time // 60
all_play_time_mins = left_time % 60

if all_play_time > time_needed:
    print("Tom will run away")
    print(f"{all_play_time_hours} hours and {all_play_time_mins:01} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{all_play_time_hours} hours and {all_play_time_mins:01} minutes less for play")
