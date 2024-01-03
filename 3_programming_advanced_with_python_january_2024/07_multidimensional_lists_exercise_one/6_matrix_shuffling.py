rows, cols = [int(x) for x in input().split()]

matrix = [[str(x) for x in input().split()] for _ in range(rows)]

current_command = input()

while current_command != "END":
    command = current_command.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
    elif command[0] == "swap":
        fp_row_index, fp_col_index, sp_row_index, sp_col_index = [int(x) for x in (command[1:])]
        if 0 <= fp_row_index < rows and 0 <= fp_col_index < cols and \
                0 <= sp_row_index < rows and 0 <= sp_col_index < cols:
            matrix[fp_row_index][fp_col_index], matrix[sp_row_index][sp_col_index] = \
                matrix[sp_row_index][sp_col_index], matrix[fp_row_index][fp_col_index]
            for current_row in matrix:
                print(' '.join(current_row))
        else:
            print("Invalid input!")

    current_command = input()
