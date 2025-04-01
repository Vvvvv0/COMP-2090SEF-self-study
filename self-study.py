class Heap:
    def __init__(self, heap_type='min'):
        """ 
        Initialize a heap. Default is min-heap.
        heap_type: min for min-heap, max for max-heap 
        """
        self.heap = []
        self.type = heap_type.lower()
        if self.type not in ['min', 'max']:
            raise ValueError("Heap type must be either 'min' or 'max'")
        
    def parent(self, i):
        """Return the index of the parent of node i"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Return the index of the left child of node i"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Return the index of the right child of node i"""
        return 2 * i + 2
    
    def compare(self, a, b):
        """Compare two elements based on heap type"""
        if self.type == 'min':
            return a < b
        else:
            return a > b
        
    def insert(self, key):
        """Insert a new key into the heap"""
        self.heap.append(key)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, i):
        """Move the element at index i up to its correct position"""
        while i > 0 and self.compare(self.heap[i], self.heap[self.parent(i)]):
            """Swap with parent"""
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract(self):
        """
        Remove and return the min (min-heap) or max (max-heap) element
        Returns None if heap is empty
        """
        if not self.heap:
            return None
        
        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last 
            self.bubble_down(0)

        return root
    
    def bubble_down(self, i):
        """Move the element at index i down to its correct position"""
        size = len(self.heap)
        extreme = i # Initialize extreme as current node

        while True:
            left = self.left_child(i)
            right = self.right_child(i)

            if left < size and self.compare(self.heap[left], self.heap[extreme]):
                extreme = left

            if right < size and self.compare(self.heap[right], self.heap[extreme]):
                extreme = right

            if extreme != i:
                """Swap with the more extreme child"""
                print(f"Swapping {self.heap[i]} with {self.heap[extreme]}")  # Debugging print statement
                self.heap[i], self.heap[extreme] = self.heap[extreme], self.heap[i]
                i = extreme  # Update i to extreme
            else:
                break

    def peek(self):
        """Get the min/max element without removing it"""
        return self.heap[0] if self.heap else None
    
    def size(self):
        """Return the number of elements in the heap"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if the heap is empty"""
        return len(self.heap) == 0
    
    def heapify(self, arr):
        """Build a heap from an array"""
        self.heap = arr.copy()
        # Start from the last non-leaf node and sift down each
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.bubble_down(i)
        
    def __str__(self):
        return str(self.heap)
    
min_heap = Heap('min')
min_heap.insert(7)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)
min_heap.insert(5)
print("\nMin-heap:", min_heap) # Min-heap: [1, 3, 8, 7, 5]
print("Extract min:", min_heap.extract()) # Extract min: 1
print("Heap after extraction:", min_heap) # Heap after extraction: [3, 5, 8, 7]

max_heap = Heap('max')
max_heap.heapify([7, 3, 8, 1, 5])
print("\nMax-heap:", max_heap) # Max-heap: [8, 5, 7, 1, 3]
print("Peek max:", max_heap.peek()) # Peek max: 8
print("Extract max:", max_heap.extract()) # Extract max: 8
print("Heap after extraction:", max_heap, '\n') # Heap after extraction: [7, 5, 3, 1]



