rows, columns = [int(x) for x in input().split(", ")]

matrix = []
sum_matrix = 0

for row in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)
    sum_matrix += sum(numbers)

print(sum_matrix)
print(matrix)

# Second solution:
# rows, columns = [int(x) for x in input().split(", ")]
#
# matrix = []
# sum_matrix = 0
#
# for row in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])
#
# for row_index in range(rows):
#     for column_index in range(columns):
#         sum_matrix += matrix[row_index][column_index]
#
# print(sum_matrix)
# print(matrix)
