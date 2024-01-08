import heapq

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


def shortest_path(graph, start, target=''):
    """A funciton that determines the shortest path between nodes. 
        :params: graph: dictionary - a dictionary of nodes that lists the next corresponding node and its distance
        :params: start: string - the key of the key:value pair in the graph
        :return distances, paths: dictionary - the dictionaries of the distances and paths for each node  """
    heap = [(0, start)] #start with the start node with a distance of 0
    visited = set()
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while heap:
        current_distance, current = heapq.heappop(heap) #get node with smallest distance
        if current in visited:
            continue #skip if already visited
        visited.add(current)

        for node, distance in graph[current]:
            # if distance + distances[current] < distances[node]:
            if node not in visited:
                new_distance = current_distance + distance
                if new_distance < distances[node]:
                    distances[node] = new_distance
                    # check if shorter path exsits and updates path.
                    paths[node] = paths[current][:]
                    paths[node].append(node)
                    heapq.heappush(heap,(new_distance, node)) #add or update node in heap

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths


shortest_path(my_graph, 'A', 'F')
