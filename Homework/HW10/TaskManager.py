class Entry:
    """Represents an entry in the priority queue."""

    def __init__(self, priority, process_id):
        """Initializes an Entry object with a given priority and process ID."""
        self.priority = priority
        self.process_id = process_id

    def __repr__(self):
        """Returns a string representation of the Entry object."""
        return f"Entry(priority={self.priority}, process_id={self.process_id})"

    ####### Implement all Entry class methods under this line #######
    def __gt__(self, other):
        """Compares the priority of this entry with another entry.
        Returns:bool: True if this entry has higher priority than the other, False otherwise."""
        return self.priority > other.priority
    
    def __eq__(self, other):
        """Checks if this entry is eq   ual to another entry based on priority.
        Returns:bool: True if the priorities are equal, False otherwise."""
        return self.process_id == other.process_id and self.priority == other.priority
    

class MaxHeap:
    """Represents a max heap data structure."""

    def __init__(self):
        """Initializes a MaxHeap object."""
        self._heap = []

    ####### Implement all MaxHeap class methods under this line #######
    def put(self, entry):
        """Inserts an entry into the max heap."""
        self._heap.append(entry)
    
        i = len(self._heap) - 1

        while i > 1 and self._heap[i // 2] < self._heap[i]:
            temp = self._heap[i]
            self._heap[i] = self._heap[i//2]
            self._heap[i//2] = temp
            i = i // 2

    def remove_max(self):
        """Removes and returns the entry with the maximum priority from the max heap.
        Returns:The process ID that was removed from the queue. raise IndexError if the heap is empty"""
        if len(self._heap) == 0:
            raise IndexError
        returner = self._heap[0].process_id
        self._downheap(0)
        return returner
    
    def change_priority(self, process_id, new_priority):
        """Changes the priority of a process in the max heap.
        Returns:bool: True if the priority change was successful, False otherwise."""
        

    def _upheap(self, index):
        """Performs up-heap operation to maintain heap property after insertion."""
        i = index

        while i > len(self._heap)-1:
            temp = self._heap[i]
            self._heap[i] = self._heap[i//2]
            self._heap[i // 2] = temp
            i = i // 2 
 
    def _downheap(self, index):
        """Performs down-heap operation to maintain heap property after removal."""
        i = index
        while i < len(self._heap)-1:
            temp = self._heap[i]
            self._heap[i] = self._heap[i*2]
            self._heap[i*2] = temp
            i = i * 2   

    def __len__(self):
        """len is number of items in PQ"""    
        return len(self._heap)      

class TaskManager:
    """Manages the execution of processes using a priority queue."""

    def __init__(self):
        """Initializes a TaskManager object."""
        self.processor_queue = MaxHeap()
    
    ####### Implement all TaskManager class methods under this line #######
    def add_process(self, entry):
        """Adds a process to the processor queue."""

    def remove_process(self):
        """Removes and returns the process with the highest priority from the processor queue."""

