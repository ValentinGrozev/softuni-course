rows = columns = int(input())

matrix = [[int(x) for x in input().split(", ")]for _ in range(rows)]

primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")


# Second solution:
#
# rows = columns = int(input())
#
# matrix = [[int(x) for x in input().split(", ")]for _ in range(rows)]
#
# primary_diagonal = []
# secondary_diagonal = []
#
# for row in range(rows):
#     primary_diagonal.append(matrix[row][row])
#
# for row in range(rows):
#     secondary_diagonal.append(matrix[row][rows - row - 1])
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
