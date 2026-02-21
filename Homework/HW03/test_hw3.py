import unittest
import hw3

class test_hw3(unittest.TestCase):

    def setUp(self):
        self.l1 = [1,2,3,4,5,7]
        self.l2 = [1,2,3,4,5,6]


    def check_generate_list(self):
        self.size = 10
        self.l1,self.l2 = hw3.generate_lists(self.size)
        self.assertEqual(len(self.l1),10)
        self.assertEqual(len(self.l1),10)

    def check_find_common(self):
        self.assertEqual(hw3.find_common(self.l1,self.l2),1)

    def check_find_common_efficient(self):
        self.assertEqual(hw3.find_common_efficient(self.l1,self.l2), 1)

    

        
