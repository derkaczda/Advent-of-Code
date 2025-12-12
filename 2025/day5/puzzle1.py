
import os.path as osp

def identify_fresh_ingredients(input):
    split_index = input.index("")
    ranges, ingredients = input[:split_index], input[split_index+1:]
    all_fresh_ingredients = 0
    ranges = [list(map(int, r.split('-'))) for r in ranges]
    # Iterate over all ingredients and check
    # if we can find a valid range for it.
    for ing in ingredients:
        for start, end in ranges:
            if start <= int(ing) <= end:
                all_fresh_ingredients += 1
                break

    return all_fresh_ingredients

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()

    print (identify_fresh_ingredients(lines))