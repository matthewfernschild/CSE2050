class Node:
    '''
        Initialize node with:
        item = Any
        link = None | Node
    '''
    def __init__(self,item,link=None):
        '''link is optional. no link makes it None'''
        self.item = item
        self.link = link
    
    def __repr__(self):
        '''
        this is how the class returns if called as a strings
        why is it making me put a docstring for a dundermethod. 
        '''
        return f"Node({self.item})"
    
class LinkedList:
    def __init__(self,items=None):
        '''Items is optional'''
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for x in items:
                self.add_last(x)
        
    def __len__(self):
        '''LENGTH'''
        return self._len
    def get_head(self):
        '''
        Docstring for get_head
        
        gets the head
        '''
        return None if self._head is None else self._head.item
    def get_tail(self):
        '''
        Docstring for get_tail
        
        gets the tail
        '''
        return None if self._tail is None else self._tail.item
    def add_last(self, item):
        '''
        add to end
        '''
        new_node = Node(item, None)

        if self._head is None:         
            self._head = new_node
            self._tail = new_node
        else:                          
            self._tail.link = new_node
            self._tail = new_node

        self._len += 1

    def add_first(self,item):
        '''
        add to beginning'''
        new_node = Node(item, self._head)
        self._head = new_node

        if self._tail is None:        
            self._tail = new_node

        self._len += 1

    def remove_first(self):
        '''removes from beginning'''
        if self._head is None:
            raise RuntimeError("LinkedList is empty")

        removed_item = self._head.item
        self._head = self._head.link
        self._len -= 1

        if self._len == 0:
            self._tail = None

        return removed_item

    def remove_last(self):
        '''removes from end'''
        if self._head is None:
            raise RuntimeError("LinkedList is empty")

        # only one node
        if self._head.link is None:
            removed_item = self._head.item
            self._head = None
            self._tail = None
            self._len = 0
            return removed_item

        # find node before tail
        prev = self._head
        while prev.link is not self._tail:
            prev = prev.link

        removed_item = self._tail.item
        prev.link = None
        self._tail = prev
        self._len -= 1

        return removed_item