import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import puzzle2

class Puzzle2Test(unittest.TestCase):

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
        self.assertEqual (puzzle2.unlock_safe(input), 6, "Should be 6")

    def test_multi_visit_one_rotation_positive(self):
        input = ["R1000"]
        self.assertEqual (puzzle2.unlock_safe(input), 10, "Should be 10")

    def test_multi_visit_one_rotation_negative(self):
        input = ["L1000"]
        self.assertEqual (puzzle2.unlock_safe(input), 10, "Should be 10")

    def test_left_rotation_to_zero (self):
        input = ["L50"]
        self.assertEqual (puzzle2.unlock_safe(input), 1, "Should be 1")
        input = ["L150"]
        self.assertEqual (puzzle2.unlock_safe(input), 2, "Should be 2")

    def test_right_rotation_to_zero (self):
        input = ["R50"]
        self.assertEqual (puzzle2.unlock_safe(input), 1, "Should be 1")
        input = ["R150"]
        self.assertEqual (puzzle2.unlock_safe(input), 2, "Should be 2")

    def test_left_rotation_from_zero (self):
        input = ["L50", "L1"]
        self.assertEqual (puzzle2.unlock_safe(input), 1)
        input = ["L50", "L100"]
        self.assertEqual (puzzle2.unlock_safe(input), 2)
        input = ["L50", "R1", "L1"]
        self.assertEqual (puzzle2.unlock_safe(input), 2)


    def test_right_rotation_from_zero (self):
        input = ["R50", "R1"]
        self.assertEqual (puzzle2.unlock_safe(input), 1)
        input = ["R50", "R100"]
        self.assertEqual (puzzle2.unlock_safe(input), 2)
        input = ["R50", "L1", "R1"]
        self.assertEqual (puzzle2.unlock_safe(input), 2)