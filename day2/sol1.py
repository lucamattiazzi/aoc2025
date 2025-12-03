import math

with open("day2/input1.txt", "r") as file:
    ranges = file.read().strip()

ranges = ranges.split(",")

total = 0

DIVISORS = [
    [11],  ## 2 digits
    [],  ## 3 digits
    [101],  ## 4 digits
    [],  ## 5 digits
    [1001],  ## 6 digits
    [],  ## 7 digits
    [10001],  ## 8 digits
    [],  ## 9 digits
    [100001],  ## 10 digits
]


def divisible_by_at_least_one(num: int, divisors: list[int]) -> bool:
    for divisor in divisors:
        if num % divisor == 0:
            return True
    return False


for range_block in ranges:
    start, end = range_block.split("-")
    for num in range(int(start), int(end) + 1):
        total_digits = math.ceil(math.log10(num))
        divisors = DIVISORS[total_digits - 2]
        has_repeated_digits = divisible_by_at_least_one(num, divisors)
        if has_repeated_digits:
            total += num
print(total)
