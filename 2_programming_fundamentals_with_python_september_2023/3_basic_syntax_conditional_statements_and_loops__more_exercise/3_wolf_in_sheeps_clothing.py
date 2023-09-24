command = input()

new_list = command.split(", ")
wolf_position = 0

for index, animal in enumerate(new_list):
    if animal == "wolf":
        wolf_position = index
        print(wolf_position)



        # if counter < (all_animals / 2):
        #     print("Please go away and stop eating my sheep")
        # else:
        #     print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")

