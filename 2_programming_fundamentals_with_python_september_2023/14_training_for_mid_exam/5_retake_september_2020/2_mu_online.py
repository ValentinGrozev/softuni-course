dungeon_rooms_list = input().split("|")

initial_health = 100
bitcoins = 0
room_passed = 0
flag = False

for dungeon in dungeon_rooms_list:
    [command, number] = dungeon.split()
    room_passed += 1
    if command == "potion":
        healing_potion = int(number)
        current_health = initial_health + healing_potion
        if current_health > 100:
            additional_health = 100 - initial_health
            initial_health = 100
            print(f"You healed for {additional_health} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            initial_health = current_health
            print(f"You healed for {healing_potion} hp.")
            print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        bitcoins += int(number)
        print(f"You found {number} bitcoins.")
    else:
        initial_health -= int(number)
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            flag = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_passed}")
            break

if not flag:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")
