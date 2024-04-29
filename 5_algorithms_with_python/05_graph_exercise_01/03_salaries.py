def dfs(employee, current_graph):
    result = 0

    if all(flag == "N" for flag in current_graph[employee]):
        return 1

    for index, child in enumerate(current_graph[employee]):
        if child == "Y":
            result += dfs(index, current_graph)

    return result


number_of_employees = int(input())

graph = []
salary = 0

for _ in range(number_of_employees):
    graph.append(list(input()))

for row_index in range(len(graph)):
    salary += dfs(row_index, graph)

print(salary)
