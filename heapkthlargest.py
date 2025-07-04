class Heap:
    def __init__(self, arr):
        self.arr = arr.copy()  # Create a copy to avoid modifying the input array
        self.build_heap()

    def heapify(self, arr, n, i):
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
            self.heapify(arr, n, largest)

    def build_heap(self):
        # Start from last non-leaf node
        for i in range(len(self.arr) // 2 - 1, -1, -1):
            self.heapify(self.arr, len(self.arr), i)

    def find_kth_largest(self, k):
        if k < 1 or k > len(self.arr):
            raise ValueError("k is out of bounds")

        # Create a copy of the heap array
        heap = self.arr.copy()
        n = len(heap)

        # Extract max k times
        for i in range(k - 1):
            if n == 0:
                raise ValueError("Heap is empty before reaching k")
            # Move the last element to the root and reduce heap size
            heap[0], heap[n - 1] = heap[n - 1], heap[0]
            n -= 1
            # Heapify the root of the reduced heap
            self.heapify(heap, n, 0)

        # The kth largest is now at the root
        if n == 0:
            raise ValueError("Heap is empty")
        return heap[0]

    def is_max_heap(self, arr=None):
        # Default to self.arr if no array is provided
        if arr is None:
            arr = self.arr

        n = len(arr)
        if n <= 1:  # Empty or single-element arrays are max-heaps
            return True

        # Check all non-leaf nodes
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2

            # Check left child (if it exists)
            if left < n and arr[i] < arr[left]:
                return False

            # Check right child (if it exists)
            if right < n and arr[i] < arr[right]:
                return False

        return True


# Test the heap, kth largest, and is_max_heap methods
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    heap = Heap(arr)
    print("Original array:", arr)
    print("Max heap array:", heap.arr)
    print("Is max heap (self.arr):", heap.is_max_heap())
    k = 2
    result = heap.find_kth_largest(k)
    print(f"{k}th largest value:", result)

    # Test is_max_heap with other arrays
    test_heap = [10, 5, 3, 4, 1]  # Valid max-heap
    test_non_heap = [4, 10, 3, 5, 1]  # Not a max-heap
    print("Is [10, 5, 3, 4, 1] a max heap?", heap.is_max_heap(test_heap))
    print("Is [4, 10, 3, 5, 1] a max heap?", heap.is_max_heap(test_non_heap))
