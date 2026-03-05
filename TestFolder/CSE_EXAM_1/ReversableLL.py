from LinkedList import LinkedList

class ReversableLL(LinkedList):
   def reverse(self):
    self._tail = curr = self._head
    prev = None
    while curr is not None:
      # SAVE NEXT ITEM
      nxt = curr.link
      # CHANGE LINK TO OLD
      curr.link = prev
      # CURRENT NODE IS NOW PREV AFTER UPDATE
      prev = curr
      # CURRENT NODE IS NOW THE NEXT NODE.
      curr = nxt
    #SET DA HEAD
    self._head = prev
