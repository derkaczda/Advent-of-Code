
import os.path as osp
import itertools
import math

def do_fancy_math(input):
    def compute(values, symbol):
        if symbol == '+':
            return sum(values)
        elif symbol == '*':
            return math.prod(values)

    symbols = list(filter(None,input[-1].split(" ")))
    # Fancy oneliner to split each line at a whitespace,
    # then removing all further whitespaces in the list
    # then converting everything to int
    values = list(zip(*[list(map(int, filter(None,x.split(" ")))) for x in input[:-1]]))
    values_and_symbol = list(zip(values, symbols))
    result = sum(list(itertools.starmap(compute, values_and_symbol)))
    return result

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()


    print(do_fancy_math(lines))