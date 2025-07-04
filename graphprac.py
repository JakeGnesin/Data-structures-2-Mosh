class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node: str) -> bool:
        """Add a node to the graph if it doesn't exist."""
        if node in self.adj_list:
            return False
        self.adj_list[node] = set()
        return True

    def remove_node(self, node: str) -> bool:
        """Remove a node and all its edges from the graph."""
        if node not in self.adj_list:
            return False

        # Remove all edges pointing to this node
        for other_node in self.adj_list:
            self.adj_list[other_node].discard(node)

        # Remove the node itself
        del self.adj_list[node]
        return True

    def add_edge(self, from_node: str, to_node: str) -> bool:
        """Add an edge between two nodes."""
        # Check if both nodes exist, add them if they don't
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        # Add the edge
        if to_node not in self.adj_list[from_node]:
            self.adj_list[from_node].add(to_node)
            return True
        return False

    def remove_edge(self, from_node: str, to_node: str) -> bool:
        """Remove an edge between two nodes."""
        if from_node not in self.adj_list or to_node not in self.adj_list:
            return False

        if to_node in self.adj_list[from_node]:
            self.adj_list[from_node].discard(to_node)
            return True
        return False

    def dfs(self, start_node: str) -> list:
        """Perform depth-first search starting from start_node, returning the traversal order."""
        if start_node not in self.adj_list:
            return []

        visited = set()
        traversal_order = []

        def dfs_recursive(node: str):
            visited.add(node)
            traversal_order.append(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)
        return traversal_order

    def topological(self, start_node: str) -> list:
        """Perform topological sort starting from start_node, returning the topological order."""
        if start_node not in self.adj_list:
            return []

        visited = set()
        stack = []

        def topo_recursive(node: str):
            visited.add(node)
            # Visit all neighbors first
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    topo_recursive(neighbor)
            # Add node to stack after all neighbors are processed
            stack.append(node)

        topo_recursive(start_node)
        # Reverse the stack to get the topological order
        return stack[::-1]

    def __str__(self) -> str:
        """Return a string representation of the graph."""
        result = []
        for node in self.adj_list:
            edges = ", ".join(self.adj_list[node])
            result.append(f"{node}: [{edges}]")
        return "\n".join(result)


# Example usage:
if __name__ == "__main__":
    g = Graph()

    # Add nodes
    g.add_node("X")
    g.add_node("B")
    g.add_node("A")
    g.add_node("P")

    # Add edges
    g.add_edge("X", "B")
    g.add_edge("X", "A")
    g.add_edge("A", "P")
    g.add_edge("B", "P")

    # Print graph
    print("Graph:")
    print(g)

    # Perform topological sort starting from X
    print("\nTopological sort starting from X:")
    print(g.topological("X"))
