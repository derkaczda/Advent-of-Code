import unittest
import sys
import os
sys.path.append(os.path.dirname('..'))
import day2.puzzle1 as puzzle1

class Day2Puzzle1Test(unittest.TestCase):

    def test_num_digits(self):
        input = 1
        self.assertEqual (puzzle1.num_digits(input), 1)
        input = 8857860
        self.assertEqual (puzzle1.num_digits(input), 7)


    def test_largest_even_range(self):
        input = [
            puzzle1.num_digits(1),
            puzzle1.num_digits(20)
        ]
        self.assertEqual (puzzle1.largest_even_range(input[0], input[1]), input[1], "Should be 2")
        input = [
            puzzle1.num_digits(49),
            puzzle1.num_digits(128)
        ]
        self.assertEqual (puzzle1.largest_even_range(input[0], input[1]), input[0], "Should be 2")
        input = [
            puzzle1.num_digits(1000),
            puzzle1.num_digits(2000)
        ]
        self.assertEqual (puzzle1.largest_even_range(input[0], input[1]), input[1], "Should be 4")

    def test_sum_of_invalid_ids(self):
        input = ["998-1012"]
        self.assertEqual (puzzle1.calculate_sum_of_invalid_ids(input), 1010, "Should be 1010")
        input = ["11-22"]
        self.assertEqual (puzzle1.calculate_sum_of_invalid_ids(input), 33, "Should be 33")
        input = ["95-115"]
        self.assertEqual (puzzle1.calculate_sum_of_invalid_ids(input), 99, "Should be 99")
        input = ["1-11"]
        self.assertEqual (puzzle1.calculate_sum_of_invalid_ids(input), 11, "Should be 11")
        input = [
            "11-22","95-115","998-1012","1188511880-1188511890",
            "222220-222224","1698522-1698528","446443-446449",
            "38593856-38593862","565653-565659",
            "824824821-824824827","2121212118-2121212124"
        ]
        self.assertEqual (puzzle1.calculate_sum_of_invalid_ids(input), 1227775554, "Should be 1227775554")


    def test_uneven_range(self):
        input = ["501-921"]
        self.assertEqual (puzzle1.calculate_sum_of_invalid_ids(input), 0, "Should be 0")
        input = ["29210-60779"]
        self.assertEqual (puzzle1.calculate_sum_of_invalid_ids(input), 0, "Should be 0")
        input = ["501-921", "29210-60779"]
        self.assertEqual (puzzle1.calculate_sum_of_invalid_ids(input), 0, "Should be 0")

    def test_starting_range(self):
        input = [7337,24735]
        self.assertEqual (puzzle1.get_starting_range(input[0], input[1]), (7337, 4))
        input = [24,47]
        self.assertEqual (puzzle1.get_starting_range(input[0], input[1]), (24, 2))
        input = [979760, 1021259]
        self.assertEqual (puzzle1.get_starting_range(input[0], input[1]), (979760, 6))



