initial_energy = int(input())
distance = input()

battles_won_counter = 0
flag = False

while distance != "End of battle" and initial_energy >= 0:
    distance = int(distance)
    if distance > initial_energy:
        flag = True
        break
    else:
        initial_energy -= distance
        battles_won_counter += 1
        if battles_won_counter % 3 == 0:
            initial_energy += battles_won_counter

    distance = input()

if flag:
    print(f"Not enough energy! Game ends with {battles_won_counter} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {battles_won_counter}. Energy left: {initial_energy}")
