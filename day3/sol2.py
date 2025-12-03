with open("./day3/input1.txt") as f:
    banks = f.read().splitlines()

total = 0

DIGITS_NUMBER = 12


def find_leftmost_highest_number_idx(string: str) -> int:
    highest_number = 0
    leftmost_idx = 0
    for i in range(len(string)):
        value = int(string[i])
        if value <= highest_number:
            continue
        highest_number = value
        leftmost_idx = i
    return leftmost_idx


for bank in banks:
    partial = 0
    starts_from = 0
    for iteration in range(DIGITS_NUMBER):
        remaining = DIGITS_NUMBER - iteration - 1
        end = len(bank) - remaining
        string = bank[starts_from:end]
        digit_idx = find_leftmost_highest_number_idx(string)
        digit = int(string[digit_idx])
        starts_from += digit_idx
        starts_from += 1
        partial += digit * 10**remaining
    total += partial

print(total)
