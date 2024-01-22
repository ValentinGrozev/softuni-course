size_of_field = int(input())

field = []
bunny_position = [0, 0]

for row in range(size_of_field):
    field.append([x for x in input().split()])
    for col in range(size_of_field):
        if field[row][col] == "B":
            bunny_position = [row, col]

moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
max_number_of_eggs = float('-inf')
bunny_way = ""
final_bunny_moves = []
end_of_collecting = False

for move in moves:
    current_eggs = 0
    current_bunny_moves = []
    current_bunny_pos = bunny_position
    end_of_collecting = False
    for row in range(size_of_field):
        if end_of_collecting:
            break
        for col in range(size_of_field):
            next_row_position = current_bunny_pos[0] + moves[move][0]
            next_col_position = current_bunny_pos[1] + moves[move][1]
            if 0 <= next_row_position < size_of_field and 0 <= next_col_position < size_of_field:
                if field[next_row_position][next_col_position] == "X":
                    end_of_collecting = True
                    break
                else:
                    current_eggs += int(field[next_row_position][next_col_position])
                    current_bunny_moves.append([next_row_position, next_col_position])
                current_bunny_pos = [next_row_position, next_col_position]
            else:
                end_of_collecting = True
                break

    if current_eggs > max_number_of_eggs and current_bunny_moves:
        max_number_of_eggs = current_eggs
        final_bunny_moves = current_bunny_moves
        bunny_way = move

print(bunny_way)
[print(move) for move in final_bunny_moves]
print(max_number_of_eggs)
