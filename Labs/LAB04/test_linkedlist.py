import unittest
from linkedlist import Node, LinkedList


class TestNode(unittest.TestCase):
    '''
    testin the nodes
    '''
    def setUp(self):
        self.node1 = Node(1, None)
        self.node2 = Node(2, self.node1)

    def test_init(self):
        self.assertEqual(self.node1.item, 1)
        self.assertIsNone(self.node1.link)

        self.assertEqual(self.node2.item, 2)
        self.assertEqual(self.node2.link, self.node1)

    def test_repr(self):
        self.assertEqual(repr(self.node1), "Node(item=1, link=None)")
        self.assertEqual(repr(self.node2), "Node(item=2, link=Node(item=1, link=None))")


class TestLinkedList(unittest.TestCase):
    ''' 
    Struggled a bit with testcases for this. Chat helped a lot. 
    Learned new testcases (assertIsNone & assertRaises)
    '''
    def setUp(self):
        # preset datasets
        self.addlast_data = [10, 20, 30]
        self.addfirst_data = [1, 2, 3]
        self.remove_data = [1, 2, 3, 4]
        self.init_list = ['a', 'b', 'c']
        self.init_range = range(10)

        # LinkedLists created in setUp (fresh each test run)
        self.LL_empty = LinkedList()
        self.LL_letters = LinkedList(self.init_list)
        self.LL_range = LinkedList(self.init_range)

        # empty lists to mutate for add tests
        self.LL_addlast = LinkedList()
        self.LL_addfirst = LinkedList()

        # non-empty lists to mutate for remove tests
        self.LL_removefirst = LinkedList(self.remove_data)
        self.LL_removelast = LinkedList(self.remove_data)

    def test_init(self):
        self.assertEqual(len(self.LL_empty), 0)
        self.assertIsNone(self.LL_empty.get_head())
        self.assertIsNone(self.LL_empty.get_tail())

        self.assertEqual(len(self.LL_letters), 3)
        self.assertEqual(self.LL_letters.get_head(), 'a')
        self.assertEqual(self.LL_letters.get_tail(), 'c')

        self.assertEqual(len(self.LL_range), 10)
        self.assertEqual(self.LL_range.get_head(), 0)
        self.assertEqual(self.LL_range.get_tail(), 9)

    def test_add_last(self):
        for i, x in enumerate(self.addlast_data):
            self.LL_addlast.add_last(x)
            self.assertEqual(len(self.LL_addlast), i + 1)
            self.assertEqual(self.LL_addlast.get_head(), self.addlast_data[0])
            self.assertEqual(self.LL_addlast.get_tail(), x)

    def test_add_first(self):
        for i, x in enumerate(self.addfirst_data):
            self.LL_addfirst.add_first(x)
            self.assertEqual(len(self.LL_addfirst), i + 1)
            self.assertEqual(self.LL_addfirst.get_head(), x)
            # tail should be the first inserted item when only using add_first
            self.assertEqual(self.LL_addfirst.get_tail(), self.addfirst_data[0])

    def test_remove_first(self):
        for i in range(len(self.remove_data)):
            removed = self.LL_removefirst.remove_first()
            self.assertEqual(removed, self.remove_data[i])
            self.assertEqual(len(self.LL_removefirst), len(self.remove_data) - i - 1)

            if len(self.LL_removefirst) == 0:
                self.assertIsNone(self.LL_removefirst.get_head())
                self.assertIsNone(self.LL_removefirst.get_tail())
            else:
                self.assertEqual(self.LL_removefirst.get_head(), self.remove_data[i + 1])
                self.assertEqual(self.LL_removefirst.get_tail(), self.remove_data[-1])

        with self.assertRaises(RuntimeError):
            self.LL_removefirst.remove_first()

    def test_remove_last(self):
        for i in range(len(self.remove_data)):
            removed = self.LL_removelast.remove_last()
            self.assertEqual(removed, self.remove_data[-1 - i])
            self.assertEqual(len(self.LL_removelast), len(self.remove_data) - i - 1)

            if len(self.LL_removelast) == 0:
                self.assertIsNone(self.LL_removelast.get_head())
                self.assertIsNone(self.LL_removelast.get_tail())
            else:
                self.assertEqual(self.LL_removelast.get_head(), self.remove_data[0])
                self.assertEqual(self.LL_removelast.get_tail(), self.remove_data[-2 - i])

        with self.assertRaises(RuntimeError):
            self.LL_removelast.remove_last()


if __name__ == "__main__":
    unittest.main()
