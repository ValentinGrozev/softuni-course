def find_dependency(curr_graph):
    result = {}
    for node, children in curr_graph.items():
        if node not in result:
            result[node] = 0
        for curr_child in children:
            if curr_child not in result:
                result[curr_child] = 1
            else:
                result[curr_child] += 1
    return result


def find_node_with_zero_dependency(dependency_dict):
    for node, value in dependency_dict.items():
        if value == 0:
            return node
    return None


number_of_nodes = int(input())
graph = {}
topological_sorting = []

for _ in range(number_of_nodes):
    nodes_and_edges = input().split("->")
    nodes = nodes_and_edges[0].strip()
    edges = nodes_and_edges[1].strip().split(", ") if nodes_and_edges[1] else []

    graph[nodes] = edges

dependency = find_dependency(graph)
found_cycles = False

while dependency:
    node_to_remove = find_node_with_zero_dependency(dependency)

    if node_to_remove is None:
        print("Invalid topological sorting")
        found_cycles = True
        break
    else:
        for child in graph[node_to_remove]:
            dependency[child] -= 1
        dependency.pop(node_to_remove)
        topological_sorting.append(node_to_remove)

if not found_cycles:
    print(f"Topological sorting: {', '.join(x for x in topological_sorting)}")
