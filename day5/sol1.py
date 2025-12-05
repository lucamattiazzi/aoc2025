with open("./day5/input1.txt") as f:
    lines = f.read()

ranges, ids = lines.split("\n\n")

ranges = ranges.split("\n")
all_fresh_ranges = []

for current_range in ranges:
    start, end = current_range.split("-")
    all_fresh_ranges.append((int(start), int(end)))

fresh_ids = 0


def is_id_fresh(idx: int, all_fresh_ranges: list[tuple[int, int]]):
    for fresh_range in all_fresh_ranges:
        start, end = fresh_range
        if idx >= start and idx <= end:
            return True


for idx in ids.split("\n"):
    is_fresh = is_id_fresh(int(idx), all_fresh_ranges)
    if is_fresh:
        fresh_ids += 1


print(fresh_ids)
