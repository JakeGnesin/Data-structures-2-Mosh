class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[parent] > self.heap[i]:
            self.swap(i, parent)
            self._sift_up(parent)

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def _sift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)

    def sort_descending(self):
        # Create a copy of the heap to avoid modifying the original
        temp_heap = MinHeap()
        temp_heap.heap = self.heap.copy()

        # Extract all elements by repeatedly removing the root
        sorted_list = []
        while temp_heap.heap:
            sorted_list.append(temp_heap.remove())

        # Reverse to get descending order
        return sorted_list[::-1]

    def __str__(self):
        return str(self.heap)


# Example usage:
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(4)
    heap.insert(2)
    print(heap)  # [1, 2, 4, 3]
    print(heap.remove())  # 1
    print(heap)  # [2, 3, 4]
    print(heap.sort_descending())  # [4, 3, 2]
    heap.insert(7)
    heap.insert(11)
    heap.insert(16)
    heap.insert(20)
    heap.insert(18)
    heap.insert(19)
    print(heap)
    heap.insert(25)
    heap.insert(10)
    print(heap)
    print(heap.sort_descending())


# heapify
def heapify(arr, i):
    n = len(arr)  # Get the size of the array
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Compare left child with root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare right child with largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, largest)

# Function to build the heap


def build_heap(arr):
    # Start from last non-leaf node
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i)


# Test the heapify algorithm
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print("Original array:", arr)
    build_heap(arr)
    print("Max heap array:", arr)
