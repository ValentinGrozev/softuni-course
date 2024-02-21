def upper_part(number):
    for row in range(1, number + 1):
        print(f"{' ' * (number - row)}{'* ' * row}")


def down_part(number):
    for row in range(number, 1, -1):
        print(f"{' ' * (number + 1 - row)}{'* ' * (row - 1)}")


number_of_rows = int(input())

upper_part(number_of_rows)
down_part(number_of_rows)
