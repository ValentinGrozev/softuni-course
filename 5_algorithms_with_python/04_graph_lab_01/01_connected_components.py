def dfs(curr_node, curr_graph, visited_graph, component):
    if visited_graph[curr_node]:
        return

    visited_graph[curr_node] = True

    for child in curr_graph[curr_node]:
        dfs(child, curr_graph, visited_graph, component)
    component.append(curr_node)


number_of_nodes = int(input())
graph = [[int(x) for x in input().split()]for _ in range(number_of_nodes)]

visited = [False] * number_of_nodes

for node in range(number_of_nodes):
    if visited[node]:
        continue
    components = []
    dfs(node, graph, visited, components)
    print(f"Connected component: {' '.join(str(x) for x in components)}")
