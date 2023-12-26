value_of_clothes = input().split()
capacity_of_rack = int(input())

rack_counter = 1
current_box_capacity = capacity_of_rack

while len(value_of_clothes) != 0:
    if current_box_capacity >= int(value_of_clothes[-1]):
        current_box_capacity -= int(value_of_clothes.pop())
    else:
        rack_counter += 1
        current_box_capacity = capacity_of_rack

print(rack_counter)
