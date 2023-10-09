sequences_of_numbers = input().split()
number_of_elements_in_list = len(sequences_of_numbers)
middle_point = int(number_of_elements_in_list / 2)

left_car_times = sequences_of_numbers[0:middle_point]
right_car_time = sequences_of_numbers[middle_point + 1:]
right_car_time.reverse()

left_car_total_time = 0
right_car_total_time = 0
winner = ""
winner_total_time = 0

for times in range(len(left_car_times)):
    time = left_car_times[times]
    if time == "0":
        left_car_total_time = left_car_total_time * 0.80
    else:
        left_car_total_time += int(time)

for times in range(len(right_car_time)):
    time = right_car_time[times]
    if time == "0":
        right_car_total_time = right_car_total_time * 0.80
    else:
        right_car_total_time += int(time)

if left_car_total_time < right_car_total_time:
    winner = "left"
    winner_total_time = left_car_total_time
else:
    winner = "right"
    winner_total_time = right_car_total_time

print(f"The winner is {winner} with total time: {winner_total_time:.1f}")
