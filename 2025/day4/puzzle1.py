
import os.path as osp
import numpy as np
from scipy.signal import convolve2d

def grid_to_bitmap(grid):
    columns = len(grid[0])-1 # because of the \n
    rows = len(grid)
    bit_grid = np.zeros((rows, columns), dtype=int)
    for idx, row in enumerate(grid):
        row_cleaned = row.strip('\n')
        bit_grid[idx,:] = [0 if x == '.' else 1 for x in row_cleaned]
    return bit_grid

def get_number_of_valid_stacks(grid):
    grid = grid_to_bitmap(grid)
    indices = grid.flatten().nonzero()[0]
    kernel = np.ones((3,3),dtype=int)
    kernel[1,1] = 0
    result = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
    return int((result.flatten()[indices] <4).sum())

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    print (get_number_of_valid_stacks(lines))
