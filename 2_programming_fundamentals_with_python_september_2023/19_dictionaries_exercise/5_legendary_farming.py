quantity_and_material = input().lower().split()
legendary_items = ["Shadowmourne", "Valanyr", "Dragonwrath"]
legendary_item_status = False

collection = {"shards": 0, "fragments": 0, "motes": 0}

while not legendary_item_status:
    for i in range(0, len(quantity_and_material), 2):
        quantity = int(quantity_and_material[i])
        material = quantity_and_material[i + 1]
        if material not in collection:
            collection[material] = 0
        collection[material] += quantity

        if collection["shards"] >= 250:
            collection["shards"] -= 250
            print(f"{legendary_items[0]} obtained!")
            legendary_item_status = True
            break
        elif collection["fragments"] >= 250:
            collection["fragments"] -= 250
            print(f"{legendary_items[1]} obtained!")
            legendary_item_status = True
            break
        elif collection["motes"] >= 250:
            collection["motes"] -= 250
            print(f"{legendary_items[2]} obtained!")
            legendary_item_status = True
            break
    if legendary_item_status:
        break

    quantity_and_material = input().lower().split()

for material, quantity in collection.items():
    print(f"{material}: {quantity}")
