import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == end:
            return cost, path

        for (adj, weight) in graph.get(node, []):
            if adj not in visited:
                heapq.heappush(queue, (cost + weight, adj, path))
    return float("inf"), []
