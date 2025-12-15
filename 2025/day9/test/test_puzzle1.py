import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day9.puzzle1 as puzzle1

class Day9Puzzle1Test(unittest.TestCase):
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
        self.assertEqual(puzzle1.solve(input), 50)
