def create_chess_table(chess_table, size):
    for row in range(size):
        chess_table.append([x for x in input()])
    return chess_table


def find_all_knights(chess_table, knights, size):
    for row in range(size):
        for col in range(size):
            if chess_table[row][col] == "K":
                knights.append([row, col])
    return knights


def maximum_attack_of_knight(chess_table, knights, size):
    max_attacks = 0
    max_knights = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for move in POSSIBLE_MOVES:
            current_move_for_row = move[0] + k_row
            current_move_for_col = move[1] + k_col
            if 0 <= current_move_for_row < size and 0 <= current_move_for_col < size:
                if chess_table[current_move_for_row][current_move_for_col] == "K":
                    hits += 1
        if hits > max_attacks:
            max_attacks = hits
            max_knights = [k_row, k_col]
    return max_attacks, max_knights


def remove_knights(knights, max_knights, chess_table):
    knights.remove(max_knights)
    chess_table[max_knights[0]][max_knights[1]] = "0"
    knight_to_remove = 1
    return knights, chess_table, knight_to_remove


POSSIBLE_MOVES = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


def main():
    size_of_board = int(input())

    chess_table = []
    knights = []

    chess_table = create_chess_table(chess_table, size_of_board)
    knights = find_all_knights(chess_table, knights, size_of_board)

    removed_knights = 0

    while True:
        max_attacks, max_knights = maximum_attack_of_knight(chess_table, knights, size_of_board)
        if max_attacks == 0:
            break
        knights, chess_table, knight_to_remove = remove_knights(knights, max_knights, chess_table)
        removed_knights += knight_to_remove

    print(removed_knights)


main()
