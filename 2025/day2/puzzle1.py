import os.path as osp
import numpy as np

def even(number):
    return number % 2 == 0

def largest_even_range(range1, range2):
    if even(range1) and not even(range2):
        return range1
    elif not even(range1) and even(range2):
        return range2
    else:
        return max(range1, range2)

def num_digits(number: int) -> int:
    return len(str(number))

def get_nth_first_digits(number, n):
    return int(str(number)[:n])

def get_starting_range(range1, range2):
    digits_range1 = num_digits(range1)
    digits_range2 = num_digits(range2)
    if not even(digits_range1):
        return range2, digits_range2
    else:
        return range1, digits_range1

def concat_num(num1, num2):
    return int(str(num1) + str(num2))

def calculate_sum_of_invalid_ids(id_ranges):
    sum = 0
    for id_range in id_ranges:
        start_and_end = id_range.split('-')
        start = int(start_and_end[0])
        end = int(start_and_end[1])
        digits_start = num_digits(start)
        digits_end = num_digits(end)
        # if both ranges are not even than
        # we cannot construct a sequence where
        # digits are repeated twice
        if not (even(digits_start) or even(digits_end)):
            continue
        # we need the largest even range to construct our sequence
        start_value, digit_count = get_starting_range(start, end)
        # e.g. given a start_value = 123456
        # we iterate over the sequence [123, 1000]

        for num in range(
            get_nth_first_digits(start_value, digit_count//2),
            pow(10, digit_count)
            ):
            concatenated_number = concat_num(num, num)
            if concatenated_number >= start_value and concatenated_number <= end:
                sum += concatenated_number
            if concatenated_number > end:
                break
    return sum


if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "puzzle1.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()
    id_ranges = lines[0].split(',')

    print (calculate_sum_of_invalid_ids(id_ranges))

    ranges = [list(map(int, pair.split("-"))) for pair in lines[0].split(",")]
    invalid = 0
    for i in range(1, 100_000):
        candidate = int(str(i) * 2)
        for lower, upper in ranges:
            if lower <= candidate <= upper:
                invalid += candidate
                break
    print(invalid)
