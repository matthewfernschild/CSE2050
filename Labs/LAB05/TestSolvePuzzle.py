from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                self.assertTrue(puzzle([2,0,0]))

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                self.assertTrue(puzzle([1,0,0]))
        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                self.assertTrue(puzzle([2,0,0,1,0]))
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                self.assertFalse(puzzle([0,1]))
                self.assertFalse(puzzle([5,0,2,0,0,0,1]))

unittest.main()