import os.path as osp
import itertools

def identify_all_possible_fresh_ingredients(input):
    split_index = input.index("")
    ranges, ingredients = input[:split_index], input[split_index+1:]
    ranges = [list(map(int, r.split('-'))) for r in ranges]
    all_fresh_ingredients = 0

    # sort the ranges that the start increases
    ranges_sorted = sorted(ranges, key=lambda x: x[0])
    last_range = -1
    for i, (start, end) in enumerate(ranges_sorted):
        is_start_contained_in_previous = False
        fully_contaiend_in_previous = False
        if i > 0:
            # If our current start is small than the last end
            # our current range is part of the previous range
            is_start_contained_in_previous = start <= ranges_sorted[last_range][1]
            is_end_contained_in_previous = end <= ranges_sorted[last_range][1]
            fully_contaiend_in_previous = is_start_contained_in_previous and is_end_contained_in_previous


        if fully_contaiend_in_previous:
            # if the current range is fully contained in the
            # previous we do nothing. This also mean that we
            # will not consider this range in the next iteration
            # as the valid previous range.
            continue

        overlap = 0
        if is_start_contained_in_previous:
            overlap = ranges_sorted[last_range][1] - start + 1

        # We add all numbers contained in the current range
        # but need to remove the overlap with the previous
        # range from our calculation.
        all_fresh_ingredients += end-start+1-overlap
        last_range = i
    return all_fresh_ingredients

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()

    print (identify_all_possible_fresh_ingredients(lines))