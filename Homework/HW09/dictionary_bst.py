class Node: 
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.height = 1
        self.left = None
        self.right = None


class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.
    
    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        self.root = None

        if entries is not None:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        self.root = self._insert(self.root, word, meaning)

 
    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """
        current = self.root
        while current is not None:
            if word == current.word:
                return current.meaning
            if word < current.word:
                current = current.left
            else:
                current = current.right
        return None

    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        result = []
        self._in_order(self.root, result)
        return result


    # Feel free to implement other helper and private methods
    def _insert(self, node, word, meaning):
        # Standard BST insert
        if node is None:
            return Node(word, meaning)

        if word < node.word:
            node.left = self._insert(node.left, word, meaning)
        elif word > node.word:
            node.right = self._insert(node.right, word, meaning)
        else:
            # Duplicate word: update meaning
            node.meaning = meaning
            return node
        
        # Update height
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        # Balance node
        balance = self._get_balance(node)

        # Left Left
        if balance > 1 and word < node.left.word:
            return self._rotate_right(node)

        # Right Right
        if balance < -1 and word > node.right.word:
            return self._rotate_left(node)

        # Left Right
        if balance > 1 and word > node.left.word:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left
        if balance < -1 and word < node.right.word:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node
    
    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append((node.word, node.meaning))
            self._in_order(node.right, result)

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y