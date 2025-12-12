import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day6.puzzle2 as puzzle2

class Day6Puzzle2Test(unittest.TestCase):
    def test_example(self):
        input = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  ",
        ]
        self.assertEqual(puzzle2.do_fancy_math(input), 3263827)