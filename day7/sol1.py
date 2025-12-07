with open("./day7/input1.txt") as f:
    lines = f.readlines()

starting_point = lines.pop(0).index("S")
rays = set([starting_point])

total_splits = 0
for line in lines:
    splitters = [idx for idx, char in enumerate(line) if char == "^"]
    if len(splitters) == 0:
        continue
    for splitter in splitters:
        if splitter in rays:
            rays.remove(splitter)
            rays.add(splitter + 1)
            rays.add(splitter - 1)
            total_splits += 1

print(total_splits)
