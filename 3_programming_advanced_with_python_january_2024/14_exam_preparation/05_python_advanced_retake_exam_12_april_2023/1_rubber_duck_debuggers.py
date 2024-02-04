from collections import deque

times_to_complete_a_task = deque([int(time) for time in input().split()])
tasks = [int(task) for task in input().split()]

prizes = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while times_to_complete_a_task and tasks:
    current_time = times_to_complete_a_task.popleft()
    current_task = tasks.pop()

    result = current_time * current_task

    if 0 <= result <= 60:
        prize = "Darth Vader Ducky"
        prizes[prize] += 1
    elif 61 <= result <= 120:
        prize = "Thor Ducky"
        prizes[prize] += 1
    elif 121 <= result <= 180:
        prize = "Big Blue Rubber Ducky"
        prizes[prize] += 1
    elif 181 <= result <= 240:
        prize = "Small Yellow Rubber Ducky"
        prizes[prize] += 1
    else:
        current_task -= 2
        tasks.append(current_task)
        times_to_complete_a_task.append(current_time)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for prize, count in prizes.items():
    print(f"{prize}: {count}")
