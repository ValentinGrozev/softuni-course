from math import ceil

number_of_people = int(input())
capacity_of_elevator_per_elevate = int(input())

if number_of_people % capacity_of_elevator_per_elevate == 0:
    courses = number_of_people / capacity_of_elevator_per_elevate
    print(f"{courses:.0f}")
elif number_of_people < capacity_of_elevator_per_elevate:
    print(1)
elif number_of_people % capacity_of_elevator_per_elevate != 0:
    courses = ceil(number_of_people / capacity_of_elevator_per_elevate)
    print(f"{courses:.0f}")

