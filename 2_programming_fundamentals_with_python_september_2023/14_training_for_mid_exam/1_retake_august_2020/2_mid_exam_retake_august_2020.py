people_waiting = int(input())
current_state_of_wagons = input().split()

current_state_of_wagons_int = [int(number) for number in current_state_of_wagons]
maximum_capacity = 4

for wagon_index in range(len(current_state_of_wagons_int)):
    current_people_in_wagon = current_state_of_wagons_int[wagon_index]
    if people_waiting >= maximum_capacity - current_people_in_wagon:
        current_state_of_wagons_int[wagon_index] = maximum_capacity
        people_waiting -= maximum_capacity - current_people_in_wagon
    else:
        current_state_of_wagons_int[wagon_index] += people_waiting
        people_waiting = 0

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    printed_wagons = [str(number) for number in current_state_of_wagons_int]
    print(f"{' '.join(printed_wagons)}")
elif people_waiting == 0:
    if current_state_of_wagons_int[-1] == maximum_capacity:
        printed_wagons = [str(number) for number in current_state_of_wagons_int]
        print(f"{' '.join(printed_wagons)}")
    else:
        print('The lift has empty spots!')
        printed_wagons = [str(number) for number in current_state_of_wagons_int]
        print(f"{' '.join(printed_wagons)}")