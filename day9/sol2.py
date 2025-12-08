with open("./day9/example.txt") as f:
    lines = f.readlines()
    coords = [tuple(map(int, line.strip().split(","))) for line in lines]


def intersect(point_1, point_2, point_3, point_4):
    x1, y1 = point_1
    x2, y2 = point_2
    x3, y3 = point_3
    x4, y4 = point_4
    m = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if m == 0:
        return False
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / m
    if ua < 0 or ua > 1:
        return False
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / m
    if ub < 0 or ub > 1:
        return False

    return True


all_lines = []
for idx, point in enumerate(coords):
    next_point = coords[(idx + 1) % len(coords)]
    all_lines.append([point, next_point])

print("all_lines", all_lines)


def intersects_polygon(p1, p2, all_lines):
    l1 = [max(p1[0], p2[0]), max(p1[1], p2[1])]
    l2 = [max(p1[0], p2[0]), min(p1[1], p2[1])]
    l3 = [min(p1[0], p2[0]), max(p1[1], p2[1])]
    l4 = [min(p1[0], p2[0]), min(p1[1], p2[1])]
    for line in all_lines:
        if intersect(*line, l1, l2):
            return True
        if intersect(*line, l2, l3):
            return True
        if intersect(*line, l2, l4):
            return True
        if intersect(*line, l4, l1):
            return True
    return False


max_area = 0
for vertex_1 in coords:
    for vertex_2 in coords:
        if vertex_1 > vertex_2:
            continue
        has_intesection = intersects_polygon(vertex_1, vertex_2, all_lines)
        if has_intesection:
            continue
        x_side = abs(vertex_1[0] - vertex_2[0])
        y_side = abs(vertex_1[1] - vertex_2[1])
        area = (x_side + 1) * (y_side + 1)
        if area > max_area:
            max_area = area
print(max_area)
