user_input = input()

coffee_counter = 0
flag = False

while user_input != "END":
    if user_input == "coding" or user_input == "dog" or user_input == "cat" or user_input == "movie":
        coffee_counter += 1
    elif user_input == "CODING" or user_input == "DOG" or user_input == "CAT" or user_input == "MOVIE":
        coffee_counter += 2
    else:
        pass
    user_input = input()

    if coffee_counter > 5:
        flag = True
        break

if flag:
    print("You need extra sleep")
else:
    print(coffee_counter)
