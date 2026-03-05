import unittest
from find_factors import find_factors
class test_find_factors(unittest.TestCase):
    def test_zero_case(self):
        self.assertEqual(find_factors([0,1]),{0:[],1:[1]})
    def test_regular_case(self):
        self.assertEqual(find_factors([1, 3, 6, 7, 18]), {1: [1], 3: [1, 3], 6: [1, 2, 3, 6], 7: [1, 7], 18: [1, 2, 3, 6, 9, 18]})
    def test_big_num(self):
        self.assertEqual(find_factors([100,1000]), {100: [1, 2, 4, 5, 10, 20, 25, 50, 100], 1000: [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]})
    def test_prime_nums(self):
        self.assertEqual(find_factors([41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]), {41: [1, 41], 43: [1, 43], 47: [1, 47], 53: [1, 53], 59: [1, 59], 61: [1, 61], 67: [1, 67], 71: [1, 71], 73: [1, 73], 79: [1, 79], 83: [1, 83], 89: [1, 89], 97: [1, 97]})

if __name__ == '__main__':
    unittest.main()