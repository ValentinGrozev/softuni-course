from math import ceil

name_of_serial = input()
duration_for_episode = int(input())
break_time = int(input())

lunch_time = 1 / 8 * break_time
relax_time = 1 / 4 * break_time

needed_time = duration_for_episode + lunch_time + relax_time
diff = abs(break_time - needed_time)
diff = ceil(diff)

if break_time >= needed_time:
    print(f"You have enough time to watch {name_of_serial} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {diff} more minutes.")