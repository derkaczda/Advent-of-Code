import unittest
import sys
import os
import numpy as np
sys.path.append(os.path.dirname('..'))
import day4.puzzle1 as puzzle1

class Day4Puzzle1Test(unittest.TestCase):
    def test_bitmap_grid(self):
        input=["..@@.@@@@.","@@@.@.@.@@"]
        output=puzzle1.grid_to_bitmap(input).reshape(-1)

        self.assertEqual(list(output),
                         list(np.array([[0,0,1,1,0,1,1,1,1,0], [1,1,1,0,1,0,1,0,1,1]], dtype=bool).reshape(-1)))


    def test_result_example_given(self):
        input = [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
        self.assertEqual(puzzle1.get_number_of_valid_stacks(input), 13)
