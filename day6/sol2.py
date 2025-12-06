import re

with open("./day6/input1.txt") as f:
    lines = f.readlines()

values = []
signs_line = lines.pop()
signs = re.split(r"\s+", signs_line.strip())
rotated_lines = list(zip(*reversed(lines)))


total = 0

for idx in range(len(signs)):
    sign = signs[idx]
    partial = 1 if sign == "*" else 0
    while True:
        if len(rotated_lines) == 0:
            break

        next_number = rotated_lines.pop(0)
        next_number = "".join(next_number).strip()
        if len(next_number) == 0:
            break
        next_number = int(next_number[::-1])
        if sign == "*":
            partial *= next_number
        else:
            partial += next_number
    total += partial

print("total", total)
