first_number = int(input())
second_number = int(input())

for number_1 in range(first_number, second_number + 1):
    for number_2 in range(first_number, second_number + 1):
        for number_3 in range(first_number, second_number + 1):
            for number_4 in range(first_number, second_number + 1):
                if number_4 % 2 != 0:
                    if (number_2 + number_3) % 2 == 0 and number_1 > number_4 and number_1 % 2 == 0:
                        print(f"{number_1}{number_2}{number_3}{number_4}", end=' ')
                else:
                    if (number_2 + number_3) % 2 == 0 and number_1 > number_4 and number_1 % 2 != 0:
                        print(f"{number_1}{number_2}{number_3}{number_4}", end=' ')