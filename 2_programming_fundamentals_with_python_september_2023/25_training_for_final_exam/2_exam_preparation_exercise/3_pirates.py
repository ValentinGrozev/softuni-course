def plunder(city_information, city, people, gold):
    print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
    city_information[city]["population"] -= people
    city_information[city]["gold"] -= gold
    if city_information[city]['population'] == 0 or city_information[city]['gold'] == 0:
        city_information.pop(city)
        print(f"{city} has been wiped off the map!")


def prosper(city_information, city, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        city_information[city]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {city_information[city]['gold']} gold.")


def main():
    city_information = {}
    city_data = input().split("||")

    while city_data[0] != "Sail":
        city = city_data[0]
        population = int(city_data[1])
        gold = int(city_data[2])
        if city not in city_information:
            city_information[city] = {"population": 0, "gold": 0}
        city_information[city]["population"] += population
        city_information[city]["gold"] += gold

        city_data = input().split("||")

    event = input().split("=>")

    while event[0] != "End":
        if event[0] == "Plunder":
            city = event[1]
            people = int(event[2])
            gold = int(event[3])
            plunder(city_information, city, people, gold)
        elif event[0] == "Prosper":
            city = event[1]
            gold = int(event[2])
            prosper(city_information, city, gold)

        event = input().split("=>")

    if len(city_information) == 0:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")
    else:
        count = len(city_information)
        print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
        for city, city_info in city_information.items():
            print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")


main()
