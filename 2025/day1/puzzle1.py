import os
import os.path as osp

def unlock_safe (input):
    dial_position = 50
    count_zero_visited = 0
    max_num_dials = 100
    for line in input:
        direction = line[0]
        clicks = int(line[1:])
        sign = 1 if direction == "R" else -1
        dial_position = (clicks * sign + dial_position) % max_num_dials
        if dial_position == 0:
            count_zero_visited += 1

    return count_zero_visited

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "puzzle1.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    print (unlock_safe(lines))