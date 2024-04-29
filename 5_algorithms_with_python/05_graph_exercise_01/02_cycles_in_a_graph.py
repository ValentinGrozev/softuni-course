def dfs(current_key, current_graph, visited_list):
    if current_key in visited_list:
        return True

    if current_key not in visited_list:
        visited_list.append(current_key)

    if current_key not in current_graph:
        return False

    for child in current_graph[current_key]:
        result = dfs(child, current_graph, visited_list)
        if result:
            return True
    return False


input_nodes = input()

graph = {}

while input_nodes != "End":
    from_node, in_node = input_nodes.split("-")
    if from_node not in graph:
        graph[from_node] = []
    graph[from_node].append(in_node)

    input_nodes = input()


for key in graph.keys():
    cycle_result = dfs(key, graph, [])
    if cycle_result:
        print("Acyclic: No")
        break
else:
    print("Acyclic: Yes")
