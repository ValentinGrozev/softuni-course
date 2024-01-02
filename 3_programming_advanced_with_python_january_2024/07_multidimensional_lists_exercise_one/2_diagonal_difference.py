rows = columns = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagonal = [matrix[row][row] for row in range(rows)]
secondary_diagonal = [matrix[row][rows - row - 1] for row in range(rows)]

diff = abs(sum(primary_diagonal) - (sum(secondary_diagonal)))
print(diff)
