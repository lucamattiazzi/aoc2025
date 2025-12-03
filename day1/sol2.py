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

    if direction == "L":
        new_position = (current - amount) % WHEEL_SIZE
        counter += amount // WHEEL_SIZE
        if new_position > current:
            counter += 1
    else:
        new_position = (current + amount) % WHEEL_SIZE
        counter += amount // WHEEL_SIZE
        if new_position < current:
            counter += 1

    current = new_position

print(counter)
