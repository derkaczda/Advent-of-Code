import os.path as osp

def highest_joltage_for_bank (bank : str) -> int:
    bank = bank.strip("\n")
    bank_length = len(bank)
    ptr_left = 0
    for idx in range(bank_length-1):
        if bank[idx] > bank[ptr_left]:
            ptr_left = idx
    ptr_right = ptr_left+1
    for idx in range(ptr_left+1, bank_length):
        if bank[idx] > bank[ptr_right]:
            ptr_right = idx
    return int(bank[ptr_left] + bank[ptr_right])

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "puzzle1.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    max_joltage = 0
    for bank in lines:
        max_joltage += highest_joltage_for_bank(bank)

    print(max_joltage)