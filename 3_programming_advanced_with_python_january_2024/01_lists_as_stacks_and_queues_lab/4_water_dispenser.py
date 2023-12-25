from collections import deque

quantity_of_water = int(input())
name = input()
names = deque()

while name != "Start":
    names.append(name)
    name = input()

command = input().split()

while command[0] != "End":
    if command[0] == "refill":
        liters = int(command[1])
        quantity_of_water += liters
    else:
        liters = int(command[0])
        current_person_name = names.popleft()
        if liters <= quantity_of_water:
            print(f"{current_person_name} got water")
            quantity_of_water -= liters
        else:
            print(f"{current_person_name} must wait")

    command = input().split()

print(f"{quantity_of_water} liters left")
