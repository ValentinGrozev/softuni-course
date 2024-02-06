def create_battlefield(size):
    battlefield = [[row for row in list(input())]for _ in range(size)]
    return battlefield


def submarine_starting_position(size, battlefield):
    for row in range(size):
        for col in range(size):
            if battlefield[row][col] == "S":
                return [row, col]


def move(current_position, command):
    next_row_move = current_position[0] + DIRECTIONS[command][0]
    next_col_move = current_position[1] + DIRECTIONS[command][1]
    return [next_row_move, next_col_move]


BATTLE_CRUISER_TO_DESTROY = 3
MAXIMUM_HITS_BY_MINE = 2
DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    size_of_the_field = int(input())
    hits_got = 0
    battle_ships_destroyed = 0

    battlefield = create_battlefield(size_of_the_field)
    submarine_current_position = submarine_starting_position(size_of_the_field, battlefield)
    battlefield[submarine_current_position[0]][submarine_current_position[1]] = "-"

    while True:
        command = input()

        next_position = move(submarine_current_position, command)

        if battlefield[next_position[0]][next_position[1]] == "*":
            submarine_current_position = next_position
            hits_got += 1
            battlefield[next_position[0]][next_position[1]] = "-"
            if hits_got > MAXIMUM_HITS_BY_MINE:
                print(f"Mission failed, U-9 disappeared! Last known coordinates "
                      f"[{next_position[0]}, {next_position[1]}]!")
                break
            else:
                continue

        elif battlefield[next_position[0]][next_position[1]] == "C":
            submarine_current_position = next_position
            battle_ships_destroyed += 1
            battlefield[next_position[0]][next_position[1]] = "-"
            if battle_ships_destroyed == BATTLE_CRUISER_TO_DESTROY:
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                break
            else:
                continue
        elif battlefield[next_position[0]][next_position[1]] == "-":
            submarine_current_position = next_position

    battlefield[next_position[0]][next_position[1]] = "S"
    print(*[''.join(row) for row in battlefield], sep='\n')


main()
