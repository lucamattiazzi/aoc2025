with open("./day7/input1.txt") as f:
    lines = [list(l.strip()) for l in f.readlines()]

lines[0] = [0 if i == "." else 1 for i in lines[0]]

for idx in range(1, len(lines)):
    current_line = lines[idx]
    previous_line = lines[idx - 1]
    new_line = [0] * len(current_line)
    for jdx in range(len(previous_line)):
        previous_total_timelines = previous_line[jdx]
        current_char = current_line[jdx]
        if previous_total_timelines == 0:
            continue
        if current_char == ".":
            new_line[jdx] += previous_total_timelines
        if current_char == "^":
            new_line[jdx - 1] += previous_total_timelines
            new_line[jdx + 1] += previous_total_timelines
    lines[idx] = new_line

print(sum(lines[-1]))
