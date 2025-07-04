# to find min spanning tree from a graph of vertices (uses prims algo)
from heapq import heappush, heappop
from collections import defaultdict
import math


def prim_mst(graph, start):
    """
    Find Minimum Spanning Tree of a graph using Prim's algorithm.

    Args:
        graph: Dictionary representing graph as adjacency list with weights
              Format: {vertex: [(neighbor, weight), ...], ...}
        start: Starting vertex for the algorithm

    Returns:
        List of edges in MST: [(vertex1, vertex2, weight), ...]
    """
    mst = []
    visited = set()
    # Priority queue to store (weight, vertex, parent)
    pq = [(0, start, None)]

    while pq:
        weight, vertex, parent = heappop(pq)

        if vertex in visited:
            continue

        visited.add(vertex)

        # Add edge to MST if not starting vertex
        if parent is not None:
            mst.append((parent, vertex, weight))

        # Explore neighbors
        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                heappush(pq, (edge_weight, neighbor, vertex))

    return mst


# Example usage
if __name__ == "__main__":
    # Example graph as adjacency list
    graph = defaultdict(list)
    edges = [
        (0, 1, 4), (0, 2, 3), (1, 2, 1),
        (1, 3, 2), (2, 3, 4), (3, 4, 2),
        (2, 4, 3)
    ]

    # Build undirected graph
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Find MST starting from vertex 0
    mst = prim_mst(graph, 0)

    # Print results
    print("Minimum Spanning Tree edges:")
    total_weight = 0
    for u, v, w in mst:
        print(f"{u} - {v}: weight {w}")
        total_weight += w
    print(f"Total MST weight: {total_weight}")
