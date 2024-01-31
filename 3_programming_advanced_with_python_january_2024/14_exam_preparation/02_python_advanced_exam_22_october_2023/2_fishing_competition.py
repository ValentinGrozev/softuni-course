def create_field(size):
    fishing_area = [[row for row in list(input())] for _ in range(size)]
    return fishing_area


def ship_position(field, size):
    for row in range(size):
        for col in range(size):
            if field[row][col] == "S":
                return [row, col]


def next_move(current_position, size, command):
    new_row_position = current_position[0] + MOVES[command][0]
    new_col_position = current_position[1] + MOVES[command][1]

    if 0 <= new_row_position < size and 0 <= new_col_position < size:
        return [new_row_position, new_col_position]
    elif not (0 <= new_row_position < size) and 0 <= new_col_position < size:
        if new_row_position < 0:
            new_row_position = size - 1
        elif new_row_position >= size:
            new_row_position = 0
        return [new_row_position, new_col_position]
    elif 0 <= new_row_position < size and not 0 <= new_col_position < size:
        if new_col_position < 0:
            new_col_position = size - 1
        elif new_col_position >= size:
            new_col_position = 0
        return [new_row_position, new_col_position]


MOVES = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    size_of_field = int(input())
    fishing_field = create_field(size_of_field)
    position_of_ship = ship_position(fishing_field, size_of_field)
    fishing_field[position_of_ship[0]][position_of_ship[1]] = "-"

    command = input()
    catch = 0
    into_whirlpool = False

    while command != "collect the nets" and catch != 20:
        position_of_ship = next_move(position_of_ship, size_of_field, command)

        if fishing_field[position_of_ship[0]][position_of_ship[1]] == "W":
            catch = 0
            into_whirlpool = True
            break
        elif fishing_field[position_of_ship[0]][position_of_ship[1]] == "-":
            pass
        else:
            catch += int(fishing_field[position_of_ship[0]][position_of_ship[1]])
            fishing_field[position_of_ship[0]][position_of_ship[1]] = "-"

        command = input()

    fishing_field[position_of_ship[0]][position_of_ship[1]] = "S"
    row_index = position_of_ship[0]
    col_index = position_of_ship[1]

    if into_whirlpool:
        print(f"You fell into a whirlpool! The ship sank and you "
              f"lost the fish you caught. Last coordinates of the ship: "
              f"[{row_index},{col_index}]")

    if catch >= 20:
        print("Success! You managed to reach the quota!")
    elif catch < 20 and not into_whirlpool:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - catch} tons of fish more.")

    if catch > 0:
        print(f"Amount of fish caught: {catch} tons.")

    if not into_whirlpool:
        for row in fishing_field:
            print("".join(row))


main()
