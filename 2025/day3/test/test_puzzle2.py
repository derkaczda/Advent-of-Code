import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day3.puzzle2 as puzzle2

class Day3Puzzle2Test(unittest.TestCase):
    def test_bank_joltage_987654321111111(self):
        input = "987654321111111"
        self.assertEqual (puzzle2.highest_joltage_for_bank(input), 987654321111, "expected 987654321111")

    def test_bank_joltage_811111111111119(self):
        input = "811111111111119"
        self.assertEqual (puzzle2.highest_joltage_for_bank(input), 811111111119, "expected 811111111119")

    def test_bank_joltage_234234234234278(self):
        input = "234234234234278"
        self.assertEqual (puzzle2.highest_joltage_for_bank(input), 434234234278, "expected 434234234278")

    def test_bank_joltage_818181911112111(self):
        input = "818181911112111"
        self.assertEqual (puzzle2.highest_joltage_for_bank(input), 888911112111, "expected 888911112111")

    # def test_bank_joltage_4942223224223134312221222433336324234433314222333723222642441142184541322622221421243432273241422334(self):
    #     input = "4942223224223134312221222433336324234433314222333723222642441142184541322622221421243432273241422334"
    #     self.assertEqual (puzzle2.highest_joltage_for_bank(input), 98, "expected 98")

    # def test_bank_joltage_12345(self):
    #     input = "12345"
    #     self.assertEqual (puzzle2.highest_joltage_for_bank(input), 45, "expected 45")

    # def test_bank_joltage_1234511111(self):
    #     input = "1234511111"
    #     self.assertEqual (puzzle2.highest_joltage_for_bank(input), 51, "expected 51")

    # def test_bank_joltage_1111112345(self):
    #     input = "1111154321"
    #     self.assertEqual (puzzle2.highest_joltage_for_bank(input), 54, "expected 54")