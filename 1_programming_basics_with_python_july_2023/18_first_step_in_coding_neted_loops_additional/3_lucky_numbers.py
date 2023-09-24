input_number = int(input())

for number_1 in range(1, 10):
    for number_2 in range(1, 10):
        for number_3 in range(1, 10):
            for number_4 in range(1, 10):
                if number_1 + number_2 == number_3 + number_4:
                    if input_number % (number_1 + number_2) == 0:
                        print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
