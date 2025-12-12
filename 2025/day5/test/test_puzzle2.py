import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day5.puzzle2 as puzzle2

class Day5Puzzle2Test(unittest.TestCase):
    def test_example(self):
        input = [
            "3-5",
            "10-14",
            "16-20",
            "12-18",
            "",
            "1",
            "5",
            "8",
            "11",
            "17",
            "32",
        ]
        self.assertEqual(puzzle2.identify_all_possible_fresh_ingredients(input), 14)

    def test_end_in_previous(self):
        input = [
            "11-19",
            "10-20",
            "",
            "1",
            "2"
        ]
        self.assertEqual(puzzle2.identify_all_possible_fresh_ingredients(input), 20-10+1)