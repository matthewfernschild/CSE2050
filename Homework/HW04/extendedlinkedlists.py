from linkedlist import Node, LinkedList # get linkedlist.py from lab
 
# Create the classes for this assignment below.

# we need to reverse the order of the list
# can i do this via sliding window? whats the most eff way?
# what if i did
# for 
class ReversableLinkedList(LinkedList):
    '''Reverses the LinkedList'''
    def reverse(self):
        ''' Reverses linked list'''
        prev = None
        curr = self._head

        self._tail = self._head
        # chatgpt helped to explain how to properly implement when i struggled
        while curr is not None:
            nxt = curr.link
            curr.link = prev
            prev = curr
            curr = nxt
            # prev is temp previous node
            # link is now the previous node, new prev is the current node once its swapped, then the new current is the next node. 
            # now go thru the loop again
            # finally, the head is set to the last selected node.
        self._head = prev
    
class SortedLinkedList(LinkedList):
    '''Put in a sorted linked list, then you can use add_sorted to add an item in order.
    Additionally, the methods add_first and add_last will raise a NotImplementedError to
    prevent breaking the sort'''
    def add_sorted(self,item):
        '''
        Assuming list is sorted, we iterate until we find an item bigger or equal to the item.
        Then, insert the new node BEFORE it.'''
        def __init__(self, items=None):
            super().__init__()   

            if items is not None:
                for x in items:
                    self.add_sorted(x) # we are required to remove the add_last function, so we have to do this instead

        # I am looking at NEXT node to find if its >= my new node, then create NEW node before that next node
        # Therefor, I need to be ready to change the link of the curr node to my new node
        # and set my new nodes link to the next node

        ### EDGE CASES
        ## EMPTY LIST
        ## FIRST ITEM IS GREATER THEN (Replacing Head)
        
        new_node = Node(item) # NEW ITEM & NODE

        # if the list is empty, set tail and head to the new node // create new node
        if self._head == None:
            self._tail = self._head = new_node
            self._len += 1
            return
        
        # if item less than the head's item, we have a new head
        if item <= self._head.item:
            new_node.link = self._head
            self._head = new_node
            self._len += 1
            return
        
        curr = self._head
        while curr.link is not None and curr.link.item < item:
            curr = curr.link

        new_node.link = curr.link
        curr.link = new_node        
        
        if new_node.link is None:
            self._tail = new_node

        self._len += 1

    def add_first(self,item):
        '''Prevents users from accidentally breaking the sortedness'''
        raise NotImplementedError(f'Use add_sorted({item}) instead')
    def add_last(self,item):
        '''Prevents users from accidentally breaking the sortedness'''
        raise NotImplementedError(f'Use add_sorted({item}) instead')
    
class UniqueLinkedList(LinkedList):
    ''' We are given a linked list then use remove_dups to remove duplicates and create a linkedlist with unique attributes'''
    def remove_dups(self):
        '''Removes duplicates from a linkedlist
        Dict of all values - item_dict
        0 for 1x occuring values
        relink nodes to next node.
        Prio deleting latest node. I.e. node 1 == node 2, del node 2'''
        ### EDGE CASES
        ## EMPTY LIST - RETURN ERROR
        if self._head == None:
            raise RuntimeError("LinkedList is empty")
        item_dict = dict()

        curr = self._head
        prev = None
        while curr is not None:
            # if curr is in dict, then its a dupe
            if curr.item in item_dict:
                item_dict[curr.item] += 1
                
                prev.link = curr.link
                self._len -= 1

                if curr is self._tail:
                    self._tail = prev
                
                curr = prev.link
            
            else: # if item isnt in dict, add it
                item_dict[curr.item] = 0
                prev = curr
                curr = curr.link
        return item_dict
            
