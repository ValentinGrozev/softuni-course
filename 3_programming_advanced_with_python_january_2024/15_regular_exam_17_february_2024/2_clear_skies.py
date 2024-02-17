def create_field(size):
    field = [[row for row in input()]for _ in range(size)]
    return field


def jet_starting_position(field, size):
    for row in range(size):
        for col in range(size):
            if field[row][col] == "J":
                return [row, col]


def next_position(jet_position, command):
    next_row_position = jet_position[0] + DIRECTIONS[command][0]
    next_col_position = jet_position[1] + DIRECTIONS[command][1]
    return [next_row_position, next_col_position]


DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    size_of_field = int(input())

    airspace_field = create_field(size_of_field)
    jet_position = jet_starting_position(airspace_field, size_of_field)

    airspace_field[jet_position[0]][jet_position[1]] = "-"
    jet_armor = 300
    enemy_airplanes = 4

    command = input()

    while command:
        jet_position = next_position(jet_position, command)

        if airspace_field[jet_position[0]][jet_position[1]] == "E":
            enemy_airplanes -= 1
            airspace_field[jet_position[0]][jet_position[1]] = "-"
            if enemy_airplanes == 0:
                print("Mission accomplished, you neutralized the aerial threat!")
                break
            else:
                jet_armor -= 100
                if jet_armor == 0:
                    print(f"Mission failed, your jetfighter was shot down! Last coordinates "
                          f"[{jet_position[0]}, {jet_position[1]}]!")
                    break
        elif airspace_field[jet_position[0]][jet_position[1]] == "R":
            jet_armor = 300
            airspace_field[jet_position[0]][jet_position[1]] = "-"

        command = input()

    airspace_field[jet_position[0]][jet_position[1]] = "J"

    print(*[''.join(row) for row in airspace_field], sep="\n")


main()
