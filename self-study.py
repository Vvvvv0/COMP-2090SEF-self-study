"""
Heap Data Structure Implementation
Includes both MinHeap and MaxHeap variants with complete documentation
"""

class MinHeap:
    """A MinHeap implementation where the smallest element is always at the root"""
    
    def __init__(self):
        """Initialize an empty heap"""
        self.heap = []
    
    def parent(self, i):
        """Return the index of the parent node of the node at index i"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Return the index of the left child of the node at index i"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Return the index of the right child of the node at index i"""
        return 2 * i + 2
    
    def heapify_down(self, i):
        """
        Maintain the min-heap property by moving the element at index i down
        until it's in the correct position
        """
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i  # Assume current node is the smallest
        n = len(self.heap)
        
        # Check if left child exists and is smaller than current node
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        # Check if right child exists and is smaller than current smallest
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        # If the smallest isn't the current node, swap and continue heapifying
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)
    
    def heapify_up(self, i):
        """
        Maintain the min-heap property by moving the element at index i up
        until it's in the correct position
        """
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap with parent if parent is larger
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    def insert(self, key):
        """Insert a new element into the heap while maintaining the heap property"""
        self.heap.append(key)  # Add at the end
        self.heapify_up(len(self.heap) - 1)  # Move it to the correct position
    
    def extract_min(self):
        """
        Remove and return the minimum element (root) from the heap
        Returns None if heap is empty
        """
        if not self.heap:
            return None
        
        root = self.heap[0]  # Store the min value
        last = self.heap.pop()  # Remove last element
        
        if self.heap:
            self.heap[0] = last  # Move last element to root
            self.heapify_down(0)  # Heapify down to maintain property
        
        return root
    
    def peek(self):
        """Return the minimum element without removing it"""
        return self.heap[0] if self.heap else None
    
    def build_heap(self, arr):
        """Build a heap from an existing array in O(n) time"""
        self.heap = arr.copy()
        n = len(self.heap)
        
        # Start from the last non-leaf node and heapify down each
        for i in range((n // 2) - 1, -1, -1):
            self.heapify_down(i)


class MaxHeap:
    """A MaxHeap implementation where the largest element is always at the root"""
    
    def __init__(self):
        """Initialize an empty heap"""
        self.heap = []
    
    def parent(self, i):
        """Return the index of the parent node of the node at index i"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Return the index of the left child of the node at index i"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Return the index of the right child of the node at index i"""
        return 2 * i + 2
    
    def heapify_down(self, i):
        """
        Maintain the max-heap property by moving the element at index i down
        until it's in the correct position
        """
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i  # Assume current node is the largest
        n = len(self.heap)
        
        # Check if left child exists and is larger than current node
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        # Check if right child exists and is larger than current largest
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        # If the largest isn't the current node, swap and continue heapifying
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)
    
    def heapify_up(self, i):
        """
        Maintain the max-heap property by moving the element at index i up
        until it's in the correct position
        """
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            # Swap with parent if parent is smaller
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    def insert(self, key):
        """Insert a new element into the heap while maintaining the heap property"""
        self.heap.append(key)  # Add at the end
        self.heapify_up(len(self.heap) - 1)  # Move it to the correct position
    
    def extract_max(self):
        """
        Remove and return the maximum element (root) from the heap
        Returns None if heap is empty
        """
        if not self.heap:
            return None
        
        root = self.heap[0]  # Store the max value
        last = self.heap.pop()  # Remove last element
        
        if self.heap:
            self.heap[0] = last  # Move last element to root
            self.heapify_down(0)  # Heapify down to maintain property
        
        return root
    
    def peek(self):
        """Return the maximum element without removing it"""
        return self.heap[0] if self.heap else None
    
    def build_heap(self, arr):
        """Build a heap from an existing array in O(n) time"""
        self.heap = arr.copy()
        n = len(self.heap)
        
        # Start from the last non-leaf node and heapify down each
        for i in range((n // 2) - 1, -1, -1):
            self.heapify_down(i)


def test_heaps():
    """Test function to demonstrate heap functionality"""
    print("=== Testing MinHeap ===")
    min_heap = MinHeap()
    test_data = [4, 10, 3, 5, 1]
    print(f"\nBuilding heap from: {test_data}")
    min_heap.build_heap(test_data)
    print(f"Heap after build: {min_heap.heap}")  # [1, 4, 3, 5, 10]
    
    print("\nInserting value 2")
    min_heap.insert(2)
    print(f"Heap after insertion: {min_heap.heap}")  # [1, 2, 3, 5, 10, 4]
    
    print(f"\nCurrent min element: {min_heap.peek()}")  # 1
    print(f"Extracted min: {min_heap.extract_min()}")  # 1
    print(f"Heap after extraction: {min_heap.heap}")  # [2, 4, 3, 5, 10]
    
    print("\n=== Testing MaxHeap ===")
    max_heap = MaxHeap()
    print(f"\nBuilding heap from: {test_data}")
    max_heap.build_heap(test_data)
    print(f"Heap after build: {max_heap.heap}")  # [10, 5, 3, 4, 1]
    
    print("\nInserting value 7")
    max_heap.insert(7)
    print(f"Heap after insertion: {max_heap.heap}")  # [10, 7, 3, 4, 1, 5]
    
    print(f"\nCurrent max element: {max_heap.peek()}")  # 10
    print(f"Extracted max: {max_heap.extract_max()}")  # 10
    print(f"Heap after extraction: {max_heap.heap}")  # [7, 5, 3, 4, 1]


if __name__ == "__main__":
    test_heaps()