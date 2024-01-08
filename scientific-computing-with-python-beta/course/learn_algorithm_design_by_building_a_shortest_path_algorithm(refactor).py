import heapq

my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


def shortest_path(graph, start, target=None):  # target is optional
    """A funciton that determines the shortest path between nodes.
    :params: graph: dictionary - a dictionary of nodes that lists the next corresponding node and its distance
    :params: start: string - the key of the key:value pair in the graph
    :params: target: string - an optional string of where are endpoint is
    :return distances, paths: dictionary - the dictionaries of the distances and paths for each node
    """
    # input validation
    if not isinstance(graph, dict) or not graph:
        raise ValueError("The graph must be a non-empty dictionary")
    if start not in graph or (target and target not in graph):
        raise ValueError("Both start and target must be nodes in the graph")

    heap = [(0, start)]  # start with the start node with a distance of 0
    visited = set()
    distances = {node: 0 if node == start else float("inf") for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while heap:
        current_distance, current = heapq.heappop(
            heap
        )  # get node with smallest distance
        if current in visited:
            continue  # skip if already visited
        visited.add(current)

        if current == target:  # check if target is reached
            break  # exit loop early as shortest path to target is found

        for node, distance in graph[current]:
            # if distance + distances[current] < distances[node]:
            if node not in visited:
                new_distance = current_distance + distance
                if new_distance < distances[node]:
                    distances[node] = new_distance
                    # check if shorter path exsits and updates path.
                    paths[node] = paths[current][:]
                    paths[node].append(node)
                    # add or update node in heap
                    heapq.heappush(heap, (new_distance, node))

    if target:
        # Return only the path and distance to the target
        return distances[target], paths[target]
    else:
        # return all distances, paths
        return distances, paths


def format_path_output(distances, paths, start, target=None):
    """Function to format the output for printing
    :params: distances, paths: dictionary - the dictionaries of the distances and paths for each node
    :params: start: string - the key of the key:value pair in the graph
    :params: target: string - an optional string of where are endpoint is
    :return distances, paths: dictionary - the dictionaries of the distances and paths for each node
    """
    output = []
    targets_to_print = [target] if target else paths.keys()
    for node in targets_to_print:
        if node == start:
            continue
        path_str = "->".join(paths[node])
        output.append(f"{start}-{node} distance: {distances[node]}\nPath: {path_str}")
    return "\n".join(output)


try:
    distances, paths = shortest_path(my_graph, "G")
    print(format_path_output(distances, paths, "G"))
except ValueError as e:
    print("Error:", e)
