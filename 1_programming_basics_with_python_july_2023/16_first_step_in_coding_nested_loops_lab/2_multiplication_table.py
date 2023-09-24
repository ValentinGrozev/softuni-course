result = 0

for first_number in range(1, 10 + 1):
    for second_number in range(1, 10 + 1):
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")