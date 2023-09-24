quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

ornament_set_price = 2
ornament_spirit_points = 5
tree_skirt_price = 5
tree_skirt_spirit_points = 3
tree_garland_price = 3
tree_garland_spirit_points = 10
tree_lights_price = 15
tree_lights_spirit_points = 17

all_cost = 0
christmas_spirit = 0
days_to_christmas = 1
days_left = days_left_until_christmas

while days_to_christmas <= days_left_until_christmas:
    while days_to_christmas < 11:
        if days_left == 0:
            break
        if days_to_christmas % 2 == 0 and days_to_christmas % 3 != 0 and days_to_christmas != 5:
            if days_to_christmas % 10 == 0:
                all_cost += (ornament_set_price + tree_lights_price) * quantity_of_decorations
                christmas_spirit += ornament_spirit_points + tree_lights_spirit_points
                christmas_spirit -= 20
                all_cost += (tree_skirt_price + tree_garland_price + tree_lights_price)
                days_to_christmas += 1
                days_left -= 1
            else:
                all_cost += ornament_set_price * quantity_of_decorations
                christmas_spirit += ornament_spirit_points
                days_to_christmas += 1
                days_left -= 1
        elif days_to_christmas % 2 == 0 and days_to_christmas % 5 == 0 and days_to_christmas % 3 != 0:
            all_cost += (ornament_set_price + tree_lights_price) * quantity_of_decorations
            christmas_spirit += ornament_spirit_points + tree_lights_spirit_points
            days_to_christmas += 1
            days_left -= 1
        elif days_to_christmas % 3 == 0 and days_to_christmas % 5 != 0 and days_to_christmas % 2 != 0:
            all_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
            christmas_spirit += tree_skirt_spirit_points + tree_garland_spirit_points
            days_to_christmas += 1
            days_left -= 1
        elif days_to_christmas % 5 == 0 and days_to_christmas % 3 != 0:
            all_cost += tree_lights_price * quantity_of_decorations
            christmas_spirit += tree_lights_spirit_points
            days_to_christmas += 1
            days_left -= 1
        elif days_to_christmas % 2 == 0 and days_to_christmas % 3 == 0 and days_to_christmas % 5 != 0:
            all_cost += (ornament_set_price + tree_skirt_price + tree_garland_price) * quantity_of_decorations
            christmas_spirit += ornament_spirit_points + tree_skirt_spirit_points + tree_garland_spirit_points
            days_to_christmas += 1
            days_left -= 1
        else:
            days_to_christmas += 1
            days_left -= 1

    while days_to_christmas >= 11:
        if days_to_christmas % 11 == 0:
            quantity_of_decorations += 2
        else:
            quantity_of_decorations = quantity_of_decorations
        if days_left == 0:
            break
        if days_to_christmas % 2 == 0 and days_to_christmas % 3 != 0:
            if days_to_christmas % 10 == 0:
                all_cost += (ornament_set_price + tree_lights_price) * quantity_of_decorations
                christmas_spirit += ornament_spirit_points + tree_lights_spirit_points
                christmas_spirit -= 20
                all_cost += (tree_skirt_price + tree_garland_price + tree_lights_price)
                days_to_christmas += 1
                days_left -= 1
            else:
                all_cost += ornament_set_price * quantity_of_decorations
                christmas_spirit += ornament_spirit_points
                days_to_christmas += 1
                days_left -= 1
        elif days_to_christmas % 2 == 0 and days_to_christmas % 5 == 0 and days_to_christmas % 3 != 0:
            all_cost += (ornament_set_price + tree_lights_price) * quantity_of_decorations
            christmas_spirit += ornament_spirit_points + tree_lights_spirit_points
            days_to_christmas += 1
            days_left -= 1
        elif days_to_christmas % 3 == 0 and days_to_christmas % 5 != 0 and days_to_christmas % 2 != 0:
            all_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
            christmas_spirit += tree_skirt_spirit_points + tree_garland_spirit_points
            days_to_christmas += 1
            days_left -= 1
        elif days_to_christmas % 5 == 0 and days_to_christmas % 3 != 0:
            all_cost += tree_lights_price * quantity_of_decorations
            christmas_spirit += tree_lights_spirit_points
            days_to_christmas += 1
            days_left -= 1
        elif days_to_christmas % 2 == 0 and days_to_christmas % 3 == 0 and days_to_christmas % 5 == 0:
            all_cost += (ornament_set_price + tree_skirt_price + tree_garland_price + tree_lights_price) * \
                quantity_of_decorations
            christmas_spirit += ornament_spirit_points + tree_skirt_spirit_points + tree_garland_spirit_points +\
                tree_lights_spirit_points + 30
            christmas_spirit -= 20
            all_cost += (tree_skirt_price + tree_garland_price + tree_lights_price)
            days_to_christmas += 1
            days_left -= 1
        elif days_to_christmas % 3 == 0 and days_to_christmas % 5 == 0:
            all_cost += (tree_skirt_price + tree_garland_price + tree_lights_price) * quantity_of_decorations
            christmas_spirit += tree_skirt_spirit_points + tree_garland_spirit_points + tree_lights_spirit_points + 30
            days_to_christmas += 1
            days_left -= 1
        elif days_to_christmas % 2 == 0 and days_to_christmas % 3 == 0:
            all_cost += (ornament_set_price + tree_skirt_price + tree_garland_price) * quantity_of_decorations
            christmas_spirit += ornament_spirit_points + tree_skirt_spirit_points + tree_garland_spirit_points
            days_to_christmas += 1
            days_left -= 1
        else:
            days_to_christmas += 1
            days_left -= 1

if days_to_christmas % 10 == 1:
    christmas_spirit -= 30

print(f"Total cost: {all_cost}")
print(f"Total spirit: {christmas_spirit}")
