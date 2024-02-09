def create_field(size):
    field = [[row for row in input().split(" ")]for _ in range(size)]
    return field


def tunnels_position(size, field):
    tunnels = []
    for row in range(size):
        for col in range(size):
            if field[row][col] == "T":
                tunnels.append([row, col])
    return tunnels


def move(car_position, command):
    next_row_move = car_position[0] + DIRECTIONS[command][0]
    next_col_move = car_position[1] + DIRECTIONS[command][1]
    return [next_row_move, next_col_move]


DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    size_of_the_field = int(input())
    race_car_number = input()

    car_position = [0, 0]
    distance_covered = 0

    racing_field = create_field(size_of_the_field)
    second_tunnel = tunnels_position(size_of_the_field, racing_field)[1]

    while True:
        command = input()

        if command == "End":
            print(f"Racing car {race_car_number} DNF.")
            racing_field[car_position[0]][car_position[1]] = "C"
            break

        car_position = move(car_position, command)

        if racing_field[car_position[0]][car_position[1]] == ".":
            distance_covered += 10

        elif racing_field[car_position[0]][car_position[1]] == "T":
            racing_field[car_position[0]][car_position[1]] = "."
            car_position = second_tunnel
            racing_field[car_position[0]][car_position[1]] = "."
            distance_covered += 30

        elif racing_field[car_position[0]][car_position[1]] == "F":
            distance_covered += 10
            racing_field[car_position[0]][car_position[1]] = "C"
            print(f"Racing car {race_car_number} finished the stage!")
            break

    racing_field[car_position[0]][car_position[1]] = "C"

    print(f"Distance covered {distance_covered} km.")
    print(*[''.join(row) for row in racing_field], sep="\n")


main()
