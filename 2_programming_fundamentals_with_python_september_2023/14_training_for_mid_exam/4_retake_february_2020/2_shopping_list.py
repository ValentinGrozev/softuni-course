list_with_products = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        item = command[1]
        if item not in list_with_products:
            list_with_products.insert(0, item)
    elif command[0] == "Unnecessary":
        item = command[1]
        if item in list_with_products:
            list_with_products.remove(item)
    elif command[0] == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in list_with_products:
            for index in range(len(list_with_products)):
                old_item_index = list_with_products.index(old_item, 0, len(list_with_products))
                list_with_products.pop(old_item_index)
                list_with_products.insert(old_item_index, new_item)
                break
    elif command[0] == "Rearrange":
        item = command[1]
        if item in list_with_products:
            list_with_products.remove(item)
            list_with_products.append(item)

    command = input()

print(", ".join(list_with_products))
