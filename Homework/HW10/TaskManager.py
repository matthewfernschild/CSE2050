class Entry:
    """Represents an entry in the priority queue."""

    def __init__(self, priority, process_id):
        """Initializes an Entry object with a given priority and process ID."""
        self.priority = priority
        self.process_id = process_id

    def __repr__(self):
        """Returns a string representation of the Entry object."""
        return f"Entry(priority={self.priority}, process_id={self.process_id})"

    def __gt__(self, other):
        """Returns True if this entry has higher priority than the other."""
        return self.priority > other.priority

    def __lt__(self, other):
        """Returns True if this entry has lower priority than the other."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Returns True if both entries have the same priority."""
        return self.priority == other.priority


class MaxHeap:
    """Represents a max heap data structure.
    Chat helped with this
    """

    def __init__(self):
        """Initializes a MaxHeap object."""
        self._heap = []

    def put(self, entry):
        """Inserts an entry into the max heap."""
        self._heap.append(entry)
        self._upheap(len(self._heap) - 1)

    def remove_max(self):
        """
        Removes and returns the process ID with the maximum priority.
        Raises IndexError if the heap is empty.
        """
        if len(self._heap) == 0:
            raise IndexError("remove_max from empty heap")

        max_entry = self._heap[0]

        last_entry = self._heap.pop()

        if len(self._heap) > 0:
            self._heap[0] = last_entry
            self._downheap(0)

        return max_entry.process_id

    def change_priority(self, process_id, new_priority):
        """
        Changes the priority of a process in the max heap.
        Returns True if successful, False otherwise.
        """
        for i in range(len(self._heap)):
            if self._heap[i].process_id == process_id:
                old_priority = self._heap[i].priority
                self._heap[i].priority = new_priority

                if new_priority > old_priority:
                    self._upheap(i)
                elif new_priority < old_priority:
                    self._downheap(i)

                return True

        return False

    def _upheap(self, index):
        """Moves an entry up until the max heap property is restored."""
        i = index

        while i > 0:
            parent = (i - 1) // 2

            if self._heap[i] > self._heap[parent]:
                self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
                i = parent
            else:
                break

    def _downheap(self, index):
        """Moves an entry down until the max heap property is restored."""
        i = index

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < len(self._heap) and self._heap[left] > self._heap[largest]:
                largest = left

            if right < len(self._heap) and self._heap[right] > self._heap[largest]:
                largest = right

            if largest != i:
                self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
                i = largest
            else:
                break

    def __len__(self):
        """Returns the number of items in the priority queue."""
        return len(self._heap)


class TaskManager:
    """Manages the execution of processes using a priority queue.
    """

    def __init__(self):
        """Initializes a TaskManager object."""
        self.processor_queue = MaxHeap()

    def add_process(self, entry):
        """Adds a process to the processor queue."""
        self.processor_queue.put(entry)

    def remove_process(self):
        """Removes and returns the process with the highest priority."""
        return self.processor_queue.remove_max()