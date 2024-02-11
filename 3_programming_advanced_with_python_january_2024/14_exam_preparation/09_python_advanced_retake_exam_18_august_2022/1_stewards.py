from collections import deque

sequence_of_seats = input().split(", ")

first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])

matched_seats = []

matches = 0
rotations = 0

while matches < 3 and rotations < 10:
    current_first_num = first_sequence.popleft()
    current_second_num = second_sequence.pop()

    ASCII_result = chr(current_first_num + current_second_num)
    first_combination = f"{current_first_num}{ASCII_result}"
    second_combination = f"{current_second_num}{ASCII_result}"

    if first_combination in sequence_of_seats and first_combination not in matched_seats:
        matches += 1
        rotations += 1
        matched_seats.append(first_combination)
    elif second_combination in sequence_of_seats and second_combination not in matched_seats:
        matches += 1
        rotations += 1
        matched_seats.append(second_combination)
    else:
        first_sequence.append(current_first_num)
        second_sequence.appendleft(current_second_num)
        rotations += 1

print(f"Seat matches: {', '.join(seat for seat in matched_seats)}")
print(f"Rotations count: {rotations}")
