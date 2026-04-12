# Import what you need
# Include unittests here. Focus on readability, including comments and docstrings.
import unittest
import RecordsMap
class TestLocalRecord(unittest.TestCase):
    def setUp(self):
        self.test1 = RecordsMap.LocalRecord((1,1))
        self.test2 = RecordsMap.LocalRecord((0,0), 10, 1, 1)
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
        self.assertEqual(self.test1 == (1,1), True)
        # Should return False
        self.assertEqual(self.test2 == (1,1), False)

    def test_add_report(self):
        """Tests whether or not max & min values are being properly updated."""
        # Should return False
        self.test1.add_report(500)
        self.assertEqual(self.test1.min, 500)
        self.assertEqual(self.test1.max, 500)

        self.test1.add_report(5)
        self.assertEqual(self.test1.min, 5)
        self.assertEqual(self.test1.max, 500)

class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """ADD DOCSTRING. Remember to test len, get, contains, and add_report"""

    def test_add_many_reports(self):
        """ADD DOCSTRING. Remember to test len, get, contains, and add_report"""

# You need to add a line here to run the unittests

if __name__ == "__main__":
    unittest.main()