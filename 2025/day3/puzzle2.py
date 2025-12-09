import os.path as osp

def highest_joltage_for_bank (bank : str) -> int:
    bank = bank.strip("\n")
    bank_length = len(bank)

    # first we create the right most possible number, i.e. the
    # last 12 digits. Then we iteratively shift the digits
    # from right to left and find the largest number possible for
    # this power of 10
    ptr_map = list(range(bank_length-1-11, bank_length, 1))
    range_end = -1
    for ptr_idx in range(len(ptr_map)):
        ptr = ptr_map[ptr_idx]
        # We only need to search from the current pointer
        # towards the left boundary. The left boundary
        # depends on the previous pointer.
        for idx in range(ptr, range_end, -1):
            if bank[idx] >= bank[ptr_map[ptr_idx]]:
                ptr_map[ptr_idx] = idx
        # limit the next range to end before the
        # current point value since our next value
        # cannot overstep this boundary
        range_end = ptr_map[ptr_idx]
    return int("".join([bank[x] for x in ptr_map]))

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "puzzle1.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    max_joltage = 0
    for bank in lines:
        max_joltage += highest_joltage_for_bank(bank)

    print(max_joltage)