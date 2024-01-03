def is_valid_index(rows, cols, index_r_1, index_c_1, index_r_2, index_c_2):
    return 0 <= index_r_1 < rows and 0 <= index_c_1 < cols and \
            0 <= index_r_2 < rows and 0 <= index_c_2 < cols


def swap_elements(matrix, index_r_1, index_c_1, index_r_2, index_c_2):
    matrix[index_r_1][index_c_1], matrix[index_r_2][index_c_2] = \
                matrix[index_r_2][index_c_2], matrix[index_r_1][index_c_1]
    return matrix


def print_matrix(matrix):
    for current_row in matrix:
        print(' '.join(current_row))


def main():
    rows, cols = [int(x) for x in input().split()]

    matrix = [[str(x) for x in input().split()] for _ in range(rows)]

    current_command = input()

    while current_command != "END":
        command = current_command.split()
        if command[0] != "swap" or len(command) != 5:
            print("Invalid input!")
        elif command[0] == "swap":
            fp_row_index, fp_col_index, sp_row_index, sp_col_index = [int(x) for x in (command[1:])]
            if is_valid_index(rows, cols, fp_row_index, fp_col_index, sp_row_index, sp_col_index):
                swap_elements(matrix, fp_row_index, fp_col_index, sp_row_index, sp_col_index)
                print_matrix(matrix)
            else:
                print("Invalid input!")

        current_command = input()


main()
