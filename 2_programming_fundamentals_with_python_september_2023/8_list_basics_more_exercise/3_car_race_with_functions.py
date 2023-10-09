def total_time(sequence_of_numbers, start, end, is_reversed):
    total_time_side = 0
    side = sequence_of_numbers[start:end]
    if is_reversed:
        side.reverse()
    for times in range(len(side)):
        time = side[times]
        if time == "0":
            total_time_side = total_time_side * 0.8
        else:
            total_time_side += int(time)
    return total_time_side


def winner(left_total_time, right_total_time):
    if left_total_time < right_total_time:
        return f"The winner is left with total time: {left_total_time:.1f}"
    else:
        return f"The winner is right with total time: {right_total_time:.1f}"


sequences_of_numbers = input().split()
number_of_elements_in_list = len(sequences_of_numbers)
middle_point = int(number_of_elements_in_list / 2)

left_car_total_time = total_time(sequences_of_numbers, 0, middle_point, False)
right_car_total_time = total_time(sequences_of_numbers, middle_point + 1, len(sequences_of_numbers), True)
print(winner(left_car_total_time, right_car_total_time))
