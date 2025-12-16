import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day9.puzzle2 as puzzle2

class Day9Puzzle2Test(unittest.TestCase):
    def test(self):
        input = [
            "7,1",
            "11,1",
            "11,7",
            "9,7",
            "9,5",
            "2,5",
            "2,3",
            "7,3"
        ]
        self.assertEqual(puzzle2.solve(input), 24)

    def test_largest_rect_only(self):
        input = [
            "9,5",
            "2,3",
        ]
        self.assertEqual(puzzle2.solve(input), 24)