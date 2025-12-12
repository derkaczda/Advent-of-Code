
import os.path as osp
import numpy as np
from functools import partial

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def count_beams(input):
    def helper_get_binary_repr(bit_masks, width):
        binary_repr_func = np.vectorize(np.binary_repr)
        return binary_repr_func(bit_masks, width)

    def convert_splitter_pos_to_binary_mask(positions):
        tmp = np.zeros(len(input[0]))
        tmp[np.array(positions)] = 1
        return tmp

    num_beams = 0
    indices_of_splitter = list(filter(None, map(partial(find, ch="^"), input)))
    # Mark the splitter positions in a binary array
    splitter_positions = list(map(convert_splitter_pos_to_binary_mask, indices_of_splitter))
    # Track the laser positions in a binary array
    laser_position = np.zeros(len(input[0]))
    laser_position[find(input[0], ch='S')[0]] = 1
    for splitter_pos in splitter_positions:
        hit_mask = np.logical_and(laser_position, splitter_pos)
        # Create a laser left and right from the hit
        hit_indices = hit_mask.nonzero()[0]
        mask = [hit_indices-1, hit_indices+1]
        # Set the new laser positions
        laser_position[mask] = 1
        # Unset the previous laser position
        laser_position[hit_indices] = 0
        num_beams += hit_mask.sum()
    return num_beams

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()

    print(count_beams(lines))
