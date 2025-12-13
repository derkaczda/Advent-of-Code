import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day7.puzzle2 as puzzle2

class Day7Puzzle2Test(unittest.TestCase):
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
        self.assertEqual(puzzle2.count_timelines(input), 40)
