class LLNode:
	def __init__(self, item, link):
		"""LL Nodes have an item and a link to the next node"""
		self.item = item
		self.link = link

	def __repr__(self):
		"""String representation of an LLNode"""
		return f"LLNode({self.item})"

class LinkedList:
	def __init__(self):
		"""Linked Lists have a head, a tail, and a length"""
		self._head = None
		self._tail = None
		self._len = 0

	def __len__(self):
		"""Returns the number of nodes in the Linked List"""
		return self._len

	def __repr__(self):
		"""String representation of a LinkedList"""
		return f"LinkedList: head-->{self._head}, tail-->{self._tail}"

	def add_first(self, item):
		"""Adds node to front of linked list"""
		self._head = LLNode(item, link=self._head)  # Create new head
		self._len += 1                              # Increment length
		if len(self) == 1: self._tail = self._head  # Update tail (edge case)

	def remove_first(self):
		"""Removes and returns first item from LL"""
		item = self._head.item                      # item in temp var
		self._head = self._head.link                # update ll.head

		self._len -= 1                              # decrement length
		if len(self) == 0: self._tail = None        # update tail (edge case)

		return item