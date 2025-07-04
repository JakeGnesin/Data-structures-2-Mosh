class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        # Add vertices if they don't exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add edges for undirected graph (bidirectional)
        self.graph[vertex1][vertex2] = weight
        self.graph[vertex2][vertex1] = weight

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            del self.graph[vertex1][vertex2]
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            del self.graph[vertex2][vertex1]

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            # Remove all edges connected to this vertex
            for adjacent in list(self.graph[vertex]):
                self.remove_edge(vertex, adjacent)
            # Remove the vertex itself
            del self.graph[vertex]

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex1 in self.graph:
            for vertex2, weight in self.graph[vertex1].items():
                # Only add edge once since graph is undirected
                if (vertex2, vertex1, weight) not in edges:
                    edges.append((vertex1, vertex2, weight))
        return edges

    def __str__(self):
        return f"Vertices: {self.get_vertices()}\nEdges: {self.get_edges()}"


# Example usage
if __name__ == "__main__":
    g = WeightedGraph()

    # Add vertices and edges
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)

    # Print the graph
    print(g)
