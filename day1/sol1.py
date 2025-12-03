with open("day1/input1.txt", "r") as file:
    lines = file.readlines()

STARTING_POINT = 50
WHEEL_SIZE = 100

current = STARTING_POINT
counter = 0

for line in lines:
    line = line.strip()
    direction = line[0]
    amount = int(line[1:])
    sign = -1 if direction == "L" else +1
    current = (current + sign * (amount % WHEEL_SIZE)) % WHEEL_SIZE
    if current == 0:
        counter += 1
    elif current < 0:
        current = WHEEL_SIZE + current
    print(current)

print(counter)
