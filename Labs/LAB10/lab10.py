# This file empty on purpose - add the correct classes/methods below
class Entry():
    '''Entry
    - Works virtually the same as a node
    - Used to add items & priorities to Priority Queues
    '''
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.item == other.item and self.priority == other.priority
    
class PQ_UL():
    '''Sorted Priority Queue'''
    def __init__(self):
        self._entries = []
    
    def __len__(self):
        return len(self._entries)
    
    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))

    def find_min(self):
        return min(self._entries)
    
    def remove_min(self):
        e = min(self._entries)
        self._entries.remove(e)
        return e

class PQ_OL():
    '''Sorted Priority Queue
    - Sorts after each entry
    '''
    def __init__(self):
        self._entries = []
    
    def __len__(self):
        return len(self._entries)
    
    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._entries.sort()

    def find_min(self):
        return min(self._entries)
    
    def remove_min(self):
        e = min(self._entries)
        self._entries.remove(e)
        return e