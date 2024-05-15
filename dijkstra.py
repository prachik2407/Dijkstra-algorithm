import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize all distances to infinity
    distances[start] = 0  # Set the distance to the starting node to 0
    queue = [(0, start)]  # Create a priority queue and add the starting node to it
    
    while queue:  # Loop until the priority queue is empty
        current_distance, current_node = heapq.heappop(queue)  # Remove the node with the smallest distance from the priority queue
        if current_distance > distances[current_node]:  # If the distance to the current node is already smaller than the distance from the priority queue, skip it
            continue
        for neighbor, weight in graph[current_node].items():  # Update the distances to all neighbors of the current node
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))  # Add the updated distance and the neighbor to the priority queue
    
    return distances
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3},
    'E': {'C': 8, 'D': 3}
}

distances = dijkstra(graph, 'A')  # Find the shortest distances from node 'A'
print(distances)  # {'A': 0, 'B': 5, 'C': 1, 'D': 6, 'E': 9}
