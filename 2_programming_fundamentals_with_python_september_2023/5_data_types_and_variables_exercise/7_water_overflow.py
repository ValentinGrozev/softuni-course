lines_to_follow = int(input())
capacity = 255

tank_fill = 0

for liters in range(lines_to_follow):
    liters_from_line = int(input())
    tank_fill += liters_from_line

    if tank_fill > capacity:
        tank_fill -= liters_from_line
        print("Insufficient capacity!")

if tank_fill <= capacity:
    print(tank_fill)




