# Import what you need
# Include unittests here. Focus on readability, including comments and docstrings.
import unittest
import RecordsMap
class TestLocalRecord(unittest.TestCase):
    def setUp(self):
        self.test1 = RecordsMap.LocalRecord((1,1))
        self.test2 = RecordsMap.LocalRecord((0,0), 10, 1, 1)
        self.test3 = RecordsMap.LocalRecord((1.111111111111,1.333333333))
    def test_init(self):
        """Tests the initialization of LocalRecord."""
        # Empty Initialization
        self.assertEqual(self.test1.max, None)
        self.assertEqual(self.test1.min, None)
        self.assertEqual(self.test1.precision, 0)

        # Full Initialization
        self.assertEqual(self.test2.max, 10)
        self.assertEqual(self.test2.min, 1)
        self.assertEqual(self.test2.precision, 1)

    def test_hash(self):
        """Tests the functionality of the hash method on LocalRecord."""
        self.assertEqual(hash(self.test1), hash((1,1)))

    def test_eq(self):
        """Tests if __eq__ is working properly or not."""
        # Should return True
        self.assertEqual(self.test1 == self.test3, True)
        # Should return False
        self.assertEqual(self.test2 == self.test1, False)


    def test_add_report(self):
        """Tests whether or not max & min values are being properly updated."""
        # First report should initialize both min and max to 500
        self.test1.add_report(500)
        self.assertEqual(self.test1.min, 500)
        self.assertEqual(self.test1.max, 500)

        self.test1.add_report(5)
        self.assertEqual(self.test1.min, 5)
        self.assertEqual(self.test1.max, 500)

class TestRecordsMap(unittest.TestCase):
    def setUp(self):
        '''setUp allows us to reuse variables similar to how __init__ works'''
        self.test1 = RecordsMap.RecordsMap()
        self.record1 = RecordsMap.LocalRecord((1,1))
        self.record2 = RecordsMap.LocalRecord((2,2))

    def test_add_one_report(self):
        """Tests the get, len, contains, and add_report methods to ensure they work"""
        self.assertEqual(self.test1._len, 0) # len p1
        self.assertEqual(self.record1 in self.test1, False) # contains p1
        with self.assertRaises(KeyError): 
            self.test1[(10,10)]     # test get p1
        self.test1.add_report((1,1), 100) # add_report
        self.assertEqual(self.test1._len, 1) # len p2
        self.assertEqual(self.record1 in self.test1, True) # contains p2
        self.assertEqual(self.test1[(1,1)],(100,100))
        
    def test_add_many_reports(self):
        """Tests multiple add_report methods using the get, len, and contains methods"""
        # FIRST ADD REPORT
        self.test1.add_report((1,1), 100) 
        self.assertEqual(self.test1._len, 1)
        self.assertEqual(self.record1 in self.test1, True) 
        self.assertEqual(self.test1[(1,1)],(100,100))

        # SECOND ADD REPORT - SAME POS
        self.test1.add_report((1,1), 10) 
        self.assertEqual(self.test1._len, 1)
        self.assertEqual(self.record1 in self.test1, True) 
        self.assertEqual(self.test1[(1,1)],(10,100))

        # THIRD ADD REPORT - DIFF POS #
        self.test1.add_report((2,2), 50) 
        self.assertEqual(self.test1._len, 2)
        self.assertEqual(self.record2 in self.test1, True) 
        self.assertEqual(self.test1[(2,2)], (50,50))

        # THREE ADDITIONAL ADD REPORTS TO TEST CONSISTENCY AFTER REHASHING
        
        self.test1.add_report((3,3), 100) 
        self.assertEqual(self.test1._len, 3)
        self.assertEqual((3,3) in self.test1, True) 
        self.assertEqual(self.test1[(3,3)], (100,100))

        self.test1.add_report((4,4), 100) 
        self.assertEqual(self.test1._len, 4)
        self.assertEqual((4,4) in self.test1, True) 
        self.assertEqual(self.test1[(4,4)], (100,100))

        self.test1.add_report((5,5), 100) 
        self.assertEqual(self.test1._len, 5)
        self.assertEqual((5,5) in self.test1, True) 
        self.assertEqual(self.test1[(5,5)],(100,100))


if __name__ == "__main__":
    unittest.main()