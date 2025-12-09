
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

def get_rolls_to_be_removed(grid):

    kernel = np.ones((3,3),dtype=int)
    kernel[1,1] = 0
    result = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
    return result

def remove_all_rolls_possible(grid):
    grid = grid_to_bitmap(grid)
    can_be_still_removed = True
    total_rolls_removed = 0
    while can_be_still_removed:
        # indices = grid.nonzero()[0]
        roll_neighbor_count = get_rolls_to_be_removed(grid)
        rolls_to_remove = np.bitwise_and(grid.flatten(), roll_neighbor_count.flatten() < 4)
        count_removed_rolls = int(rolls_to_remove.sum())
        total_rolls_removed += count_removed_rolls
        flat_grid = grid.flatten()
        flat_grid[rolls_to_remove.nonzero()[0]] = 0
        grid = flat_grid.reshape(grid.shape)
        if count_removed_rolls <= 0:
            can_be_still_removed = False
    return total_rolls_removed



if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    print(remove_all_rolls_possible(lines))