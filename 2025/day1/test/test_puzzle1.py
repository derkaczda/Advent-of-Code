import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import puzzle1

class Puzzle1Test(unittest.TestCase):

    def test_zero_visited(self):
        input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
        input = input.split('\n')
        self.assertEqual (puzzle1.unlock_safe(input), 3, "Should be 3")