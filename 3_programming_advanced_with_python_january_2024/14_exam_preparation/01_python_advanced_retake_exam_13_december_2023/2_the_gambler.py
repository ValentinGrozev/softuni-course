def create_board(size):
    board = [[row for row in list(input())]for _ in range(size)]
    return board


def find_gamer_position(size, board):
    for row in range(size):
        for col in range(size):
            if board[row][col] == "G":
                return [row, col]


def next_move(gamer_position, command):
    next_row_position = gamer_position[0] + DIRECTIONS[command][0]
    next_col_position = gamer_position[1] + DIRECTIONS[command][1]
    return [next_row_position, next_col_position]


def is_valid(gamer_position, size):
    return 0 <= gamer_position[0] < size and 0 <= gamer_position[1] < size


DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    size_of_board = int(input())
    money_amount = 100

    board = create_board(size_of_board)
    gamer_position = find_gamer_position(size_of_board, board)
    board[gamer_position[0]][gamer_position[1]] = "-"

    jackpot = False
    game_over = False

    command = input()

    while command != "end":
        gamer_position = next_move(gamer_position, command)
        if is_valid(gamer_position, size_of_board):
            if board[gamer_position[0]][gamer_position[1]] == "W":
                money_amount += 100
            elif board[gamer_position[0]][gamer_position[1]] == "P":
                money_amount -= 200
                if money_amount <= 0:
                    board[gamer_position[0]][gamer_position[1]] = "-"
                    game_over = True
                    break
            elif board[gamer_position[0]][gamer_position[1]] == "J":
                money_amount += 100000
                jackpot = True
                board[gamer_position[0]][gamer_position[1]] = "-"
                break
            board[gamer_position[0]][gamer_position[1]] = "-"
        else:
            game_over = True
            break

        command = input()

    board[gamer_position[0]][gamer_position[1]] = "G"

    if jackpot:
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {money_amount}$")
        print(*[''.join(row) for row in board], sep="\n")
    if not jackpot and money_amount > 0:
        print(f"End of the game. Total amount: {money_amount}$")
        print(*[''.join(row) for row in board], sep="\n")
    if game_over:
        print("Game over! You lost everything!")


main()
