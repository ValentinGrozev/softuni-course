from collections import deque


def bfs(start_node, curr_graph, visited_graph):
    components = set()

    if visited_graph[start_node]:
        return []

    to_visit = deque([start_node])

    while to_visit:
        current_node = to_visit.popleft()
        visited_graph[current_node] = True

        for child in curr_graph[current_node]:
            if not visited_graph[child]:
                to_visit.append(child)

        components.add(current_node)

    return components


number_of_nodes = int(input())
graph = [[int(x) for x in input().split()]for _ in range(number_of_nodes)]

visited = [False] * number_of_nodes

for node in range(number_of_nodes):
    connected_components = bfs(node, graph, visited)
    if connected_components:
        print(f"Connected component: {' '.join(str(x) for x in connected_components)}")
