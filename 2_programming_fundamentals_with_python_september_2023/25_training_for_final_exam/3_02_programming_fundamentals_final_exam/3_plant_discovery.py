number_of_plants = int(input())

plant_information = {}

for current_plant in range(number_of_plants):
    plant_details = input().split("<->")
    plant = plant_details[0]
    rarity = int(plant_details[1])
    if plant not in plant_information:
        plant_information[plant] = {'rarity': 0, 'rating': 0}
    plant_information[plant]['rarity'] = rarity

command = input().split(":")

while command[0] != "Exhibition":
    if command[0] == "Rate":
        current_plant_information = command[1].split(" - ")
        plant_name = current_plant_information[0].strip()
        plant_rating = float(current_plant_information[1])
        if plant_name in plant_information:
            if plant_information[plant_name]['rating'] > 0:
                plant_information[plant_name]['rating'] += plant_rating
                plant_information[plant_name]['rating'] /= 2
            else:
                plant_information[plant_name]['rating'] += plant_rating
        else:
            print(f"error")
    elif command[0] == "Update":
        current_plant_information = command[1].split(" - ")
        plant_name = current_plant_information[0].strip()
        plant_rarity = int(current_plant_information[1])
        if plant_name in plant_information:
            plant_information[plant_name]['rarity'] = plant_rarity
        else:
            print(f"error")
    elif command[0] == "Reset":
        plant_name = command[1].strip()
        if plant_name in plant_information:
            plant_information[plant_name]['rating'] = 0
        else:
            print(f"error")
    command = input().split(":")

print("Plants for the exhibition:")

for plant, details in plant_information.items():
    print(f"- {plant}; Rarity: {details['rarity']:.0f}; Rating: {details['rating']:.2f}")
