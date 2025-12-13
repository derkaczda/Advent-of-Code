
import os.path as osp
import numpy as np
from functools import partial

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def count_timelines(input):

    def convert_splitter_pos_to_binary_mask(positions):
        tmp = np.zeros(len(input[0]))
        tmp[np.array(positions)] = 1
        return tmp

    indices_of_splitter = list(filter(None, map(partial(find, ch="^"), input)))
    # Mark the splitter positions in a binary array
    splitter_positions = list(map(convert_splitter_pos_to_binary_mask, indices_of_splitter))
    # Track the laser positions in all timelines
    laser_positions = np.zeros(len(input[0]), dtype=int)
    laser_positions[find(input[0], ch='S')[0]] = 1
    for splitter_pos in splitter_positions:
        # identify the laser hit positions
        hit_mask = (laser_positions > 0) & np.array(splitter_pos, dtype=int)
        hit_indices = hit_mask.nonzero()[0]
        # spread the lasers to the left and right
        new_laser_positions = np.array([hit_indices-1, hit_indices+1])
        laser_values = np.tile(laser_positions[hit_indices], new_laser_positions.shape[0]).reshape(new_laser_positions.shape)
        # add the lasers of all timelines to the new
        # laser positions and reset the lasers at the current position
        np.add.at(laser_positions, new_laser_positions, laser_values)
        laser_positions[hit_indices] = 0
    return int(laser_positions.sum())

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()

    print(count_timelines(lines))
