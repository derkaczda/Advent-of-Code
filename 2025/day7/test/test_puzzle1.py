import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day7.puzzle1 as puzzle1

class Day7Puzzle1Test(unittest.TestCase):
    def test_example(self):
        input = [
".......S.......",
"...............",
".......^.......",
"...............",
"......^.^......",
"...............",
".....^.^.^.....",
"...............",
"....^.^...^....",
"...............",
"...^.^...^.^...",
"...............",
"..^...^.....^..",
"...............",
".^.^.^.^.^...^.",
"...............",
        ]
        self.assertEqual(puzzle1.count_beams(input), 21)
