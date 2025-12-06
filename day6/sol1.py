import re

with open("./day6/input1.txt") as f:
    lines = f.readlines()


values = [re.split(r"\s+", line.strip()) for line in lines]
signs = values.pop()
print("signs", values)
totals = [0 if sign == "+" else 1 for sign in signs]


for line in values:
    for idx in range(len(line)):
        value = int(line[idx])
        sign = signs[idx]
        if sign == "+":
            totals[idx] += value
        if sign == "*":
            totals[idx] *= value


print(totals)
print(sum(totals))
