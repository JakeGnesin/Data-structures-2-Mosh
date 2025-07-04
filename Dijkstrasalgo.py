import heapq
from collections import defaultdict
import math


def dijkstra(graph, start):
    # Initialize distances dictionary with infinity for all nodes except start
    distances = {node: math.inf for node in graph}
    distances[start] = 0

    # Initialize priority queue and predecessors dictionary
    pq = [(0, start)]  # (distance, node)
    predecessors = {node: None for node in graph}

    # Set to keep track of visited nodes
    visited = set()

    while pq:
        # Get node with minimum distance
        current_distance, current_node = heapq.heappop(pq)

        # Skip if already visited
        if current_node in visited:
            continue

        # Mark as visited
        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue

            # Calculate distance to neighbor through current node
            distance = current_distance + weight

            # If we found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors

# Helper function to reconstruct path from predecessors


def get_path(predecessors, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    return path[::-1]  # Reverse to get path from start to end


# Example usage
if __name__ == "__main__":
    # Graph represented as adjacency list with weights
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }

    start_node = 'A'
    distances, predecessors = dijkstra(graph, start_node)

    # Print shortest distances
    print("Shortest distances from", start_node)
    for node, distance in distances.items():
        print(f"To {node}: {distance}")
        if distance != math.inf:
            print(f"Path: {' -> '.join(get_path(predecessors, node))}")
