import os
import os.path as osp
import math

# Idee:
# nach links:
# ich berechne wie viele schritte ich bis null habe von meiner aktuell position aus
# Angenommen current_pos = 60
# L50 -> 1
# L30 -> 0
# L60 -> 1
# L150 -> 2

# diff = abs(0 - current_pos)
# if diff > steps -> kein null durchschritt
# if diff < steps -> null durchschritt
# -> aber wie oft
# - diff == steps -> 1 mal
# - diff < steps ->


def unlock_safe (input):
    dial_position = 50
    count_zero_visited = 0
    max_num_dials = 100
    for line in input:
        direction = line[0]
        clicks = int(line[1:])
        # Compute how many clicks we have left
        # until the next zero crossing. If we are exactly at 0
        # we have 100 clicks left until the next crossing.
        if dial_position == 0:
            clicks_left = 100
        elif direction == 'L':
            clicks_left = dial_position
        elif direction == 'R':
            clicks_left = max_num_dials - dial_position
        sign = 1 if direction == "R" else -1
        dial_position = (sign*clicks + dial_position) % max_num_dials

        # If we do exactly as many clicks as we have left
        # we land on zero and therefore "cross" it once
        if clicks_left == clicks:
            count_zero_visited +=1
        # otherwise we use our left clicks to hit zero
        # and therefore cross it and then compute how many
        # full circles we have left
        elif clicks_left < clicks:
            count_zero_visited += 1 + (clicks - clicks_left) // 100

    return count_zero_visited

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "puzzle1.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    print (unlock_safe(lines))