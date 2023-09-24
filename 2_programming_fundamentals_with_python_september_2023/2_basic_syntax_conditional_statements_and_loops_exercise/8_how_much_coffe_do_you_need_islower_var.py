commands = input()

coffe_counter = 0

while commands != "END":
    if commands.lower() == "coding" \
            or commands.lower() == "dog" \
            or commands.lower() == "cat" \
            or commands.lower() == "movie":
        if commands.islower():
            coffe_counter += 1
        else:
            coffe_counter += 2

    commands = input()

if coffe_counter > 5:
    print("You need extra sleep")
else:
    print(coffe_counter)