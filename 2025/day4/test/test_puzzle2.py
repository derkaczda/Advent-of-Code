import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day4.puzzle2 as puzzle2

class Day4Puzzle2Test(unittest.TestCase):
    def test_on_example_data(self):
        input = [
            "..@@.@@@@.\n",
            "@@@.@.@.@@\n",
            "@@@@@.@.@@\n",
            "@.@@@@..@.\n",
            "@@.@@@@.@@\n",
            ".@@@@@@@.@\n",
            ".@.@.@.@@@\n",
            "@.@@@.@@@@\n",
            ".@@@@@@@@.\n",
            "@.@.@@@.@.\n",
        ]
        self.assertEqual(puzzle2.remove_all_rolls_possible(input), 43)
