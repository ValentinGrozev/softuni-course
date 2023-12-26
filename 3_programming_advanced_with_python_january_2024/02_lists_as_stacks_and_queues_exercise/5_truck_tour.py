from collections import deque

number_of_petrol_pumps = int(input())
track_information = deque()
start_pump = 0
full_rotate = 0

for pump in range(number_of_petrol_pumps):
    current_fuel, distance = input().split()
    track_information.append([int(current_fuel), int(distance)])

while full_rotate < len(track_information):
    fuel = 0
    for current_pump in range(number_of_petrol_pumps):
        fuel += track_information[current_pump][0]
        distance_to_next_pump = track_information[current_pump][1]
        if fuel >= distance_to_next_pump:
            full_rotate += 1
            fuel -= distance_to_next_pump
        else:
            track_information.rotate(-1)
            start_pump += 1
            full_rotate = 0
            break

print(start_pump)
