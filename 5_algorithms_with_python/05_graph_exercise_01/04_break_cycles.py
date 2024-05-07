def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exist(source, destination, graph):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


def main():
    number_of_graphs = int(input())
    graph = {}
    edges = []

    removed_edges = []

    for _ in range(number_of_graphs):
        nodes_and_edges = input().split(" -> ")
        node = nodes_and_edges[0]
        children = nodes_and_edges[1].split(" ")

        graph[node] = children

        for child in children:
            edges.append((node, child))

    for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
        if destination not in graph[source] or source not in graph[destination]:
            continue

        graph[source].remove(destination)
        graph[destination].remove(source)

        if path_exist(source, destination, graph):
            removed_edges.append((source, destination))
        else:
            graph[source].append(destination)
            graph[destination].append(source)

    print(f"Edges to remove: {len(removed_edges)}")

    for edge, destination in removed_edges:
        print(f"{edge} - {destination}")


main()
