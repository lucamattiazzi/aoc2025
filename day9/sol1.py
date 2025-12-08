with open("./day9/input1.txt") as f:
    lines = f.readlines()
    coords = [tuple(map(int, line.strip().split(","))) for line in lines]


max_area = 0
for vertex_1 in coords:
    for vertex_2 in coords:
        x_side = abs(vertex_1[0] - vertex_2[0])
        y_side = abs(vertex_1[1] - vertex_2[1])
        area = (x_side + 1) * (y_side + 1)
        if area > max_area:
            max_area = area
print(max_area)
