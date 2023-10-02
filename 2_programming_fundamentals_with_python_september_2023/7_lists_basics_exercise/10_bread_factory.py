working_day_events = input().split("|")

all_energy = 100
coins = 100
Factory_is_open = True

for event in working_day_events:
    [type_of_event, event_value] = event.split("-")
    if type_of_event == "rest":
        current_energy = all_energy
        all_energy += int(event_value)
        if all_energy > 100:
            all_energy = 100
        gained_energy = all_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {all_energy}.")
    elif type_of_event == "order":
        if all_energy >= 30:
            all_energy -= 30
            coins += int(event_value)
            print(f"You earned {event_value} coins.")
        else:
            all_energy += 50
            print("You had to rest!")
    else:
        if coins >= int(event_value):
            coins -= int(event_value)
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            Factory_is_open = False
            break

if Factory_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {all_energy}")