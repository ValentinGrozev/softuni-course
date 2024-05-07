def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for first_node, second_node in graph:
        if node == first_node:
            dfs(second_node, graph, visited)
        elif node == second_node:
            dfs(first_node, graph, visited)


def path_exist(node, graph, nodes):
    visited = [False] * nodes
    dfs(node, graph, visited)

    if all(visited):
        return True
    return False


def main():
    number_of_nodes = int(input())
    number_of_edges = int(input())

    graph = []
    important_connections = []

    for _ in range(number_of_edges):
        node, child = input().split(" - ")

        graph.append((int(node), int(child)))

    for index, node in enumerate(graph):
        if not path_exist(node[0], graph[:index] + graph[index+1:], number_of_nodes):
            important_connections.append(node)

    sorted_important_streets = map(lambda x: ((x[1], x[0]) if x[0] > x[1] else (x[0], x[1])), important_connections)

    print("Important streets:")
    for street in sorted_important_streets:
        print(*street)


main()
