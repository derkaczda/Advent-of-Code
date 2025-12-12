
import os.path as osp
import math
import itertools


def do_fancy_math(input):
    def compute(values, symbol):
        if symbol == '+':
            return sum(values)
        elif symbol == '*':
            return math.prod(values)

    symbol_idx = 0
    symbols = list(list(filter(None,reversed(input[-1].split(" ")))))
    length = len(input[0])
    result = 0
    values = []
    for i in range(length-1, -1, -1):
        current_number = [input[x][i] for x in range(0,4) if input[x][i].isdigit()]

        if current_number != []:
            values.append(int("".join(current_number)))

        if current_number == [] or i == 0:
            # We found a gab between numbers an now
            # can compute them together
            symbol = symbols[symbol_idx]
            tmp_result = compute(values, symbol)
            result += tmp_result
            symbol_idx += 1
            values = []
    return result

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()


    print(do_fancy_math(lines))