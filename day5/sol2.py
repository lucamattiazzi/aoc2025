with open("./day5/input1.txt") as f:
    lines = f.read()

ranges, _ = lines.split("\n\n")

ranges = ranges.split("\n")
ranges = [r.split("-") for r in ranges]
ranges = [[int(r[0]), int(r[1])] for r in ranges]
all_fresh_ranges = []

sorted_ranges = sorted(ranges, key=lambda x: x[0])
total_fresh = 0

for i in range(len(sorted_ranges)):
    current_range = sorted_ranges[i]
    start, end = current_range
    for j in range(i + 1, len(sorted_ranges)):
        following_range = sorted_ranges[j]
        if following_range[0] <= end:
            following_range[0] = end + 1
    current_fresh = end - start + 1
    if current_fresh <= 0:
        continue
    total_fresh += current_fresh

print(total_fresh)
