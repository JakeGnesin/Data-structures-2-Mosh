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

    def bfs_recursive(self, start_node: str) -> list:
        """Perform breadth-first search starting from start_node using recursion, returning the traversal order."""
        if start_node not in self.adj_list:
            return []

        visited = set()
        traversal_order = []
        queue = [start_node]

        def bfs_recursive_helper():
            if not queue:
                return
            # Process the next node in the queue
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                # Add unvisited neighbors to the queue
                # Sorted for consistent order
                for neighbor in sorted(self.adj_list[node]):
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
            # Recurse on the remaining queue
            bfs_recursive_helper()

        bfs_recursive_helper()
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

    def has_cycle(self) -> bool:
        """Detect if the directed graph contains a cycle."""
        visited = set()
        rec_stack = set()  # Tracks nodes in the current recursion stack

        def cycle_dfs(node: str) -> bool:
            visited.add(node)
            rec_stack.add(node)

            # Explore neighbors
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    if cycle_dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    # Back edge found (neighbor is in current recursion stack)
                    return True

            # Remove node from recursion stack when done exploring
            rec_stack.remove(node)
            return False

        # Check all nodes to handle disconnected components
        for node in self.adj_list:
            if node not in visited:
                if cycle_dfs(node):
                    return True
        return False

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
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")

    # Add edges to form a DAG: A -> B -> C, A -> D
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("A", "D")

    # Print graph
    print("Graph (DAG):")
    print(g)

    # Check for cycle
    print("\nHas cycle:", g.has_cycle())

    # Perform DFS starting from A
    print("\nDFS traversal starting from A:")
    print(g.dfs("A"))

    # Perform BFS starting from A
    print("\nBFS traversal starting from A:")
    print(g.bfs_recursive("A"))

    # Perform topological sort starting from A
    print("\nTopological sort starting from A:")
    print(g.topological("A"))

    # Add an edge to create a cycle: C -> A
    g.add_edge("C", "A")
    print("\nGraph (with cycle C -> A):")
    print(g)

    # Check for cycle again
    print("\nHas cycle:", g.has_cycle())

    # Remove edge
    g.remove_edge("A", "B")
    print("\nAfter removing edge A->B:")
    print(g)

    # Remove node
    g.remove_node("B")
    print("\nAfter removing node B:")
    print(g)
