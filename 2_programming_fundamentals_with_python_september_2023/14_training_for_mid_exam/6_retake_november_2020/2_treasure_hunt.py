items_in_treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split()
    if command[0] == "Loot":
        for elements_index in range(1, len(command)):
            if command[elements_index] not in items_in_treasure_chest:
                items_in_treasure_chest.insert(0, command[elements_index])
    elif command[0] == "Drop":
        index_of_item = command[1]
        if 0 <= int(index_of_item) <= len(items_in_treasure_chest) - 1:
            item_name = items_in_treasure_chest[int(index_of_item)]
            items_in_treasure_chest.pop(int(index_of_item))
            items_in_treasure_chest.append(item_name)
    elif command[0] == "Steal":
        items_to_remove = int(command[1])
        if 0 <= items_to_remove < len(items_in_treasure_chest):
            removed_items = items_in_treasure_chest[-items_to_remove:]
            print(', '.join(removed_items))
            items_in_treasure_chest = items_in_treasure_chest[:-items_to_remove]
        elif items_to_remove >= len(items_in_treasure_chest):
            print(', '.join(items_in_treasure_chest))
            print("Failed treasure hunt.")
            items_in_treasure_chest.clear()

    command = input()

length_of_all_items = 0
elements_in_list = 0
for item_name in items_in_treasure_chest:
    length_of_current_item = len(item_name)
    length_of_all_items += int(length_of_current_item)
for element in items_in_treasure_chest:
    elements_in_list += 1

if length_of_all_items != 0 and elements_in_list != 0:
    average_treasure_gain = length_of_all_items / elements_in_list
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
