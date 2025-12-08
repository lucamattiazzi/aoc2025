import numpy as np
import scipy as sp

with open("./day8/input1.txt") as f:
    lines = f.readlines()
    coords = [tuple(map(int, line.strip().split(","))) for line in lines]

coords = np.array(coords)
distances = sp.spatial.distance.cdist(coords, coords)
row_indices, col_indices = np.triu_indices(distances.shape[1], 1)
triangle = distances[row_indices, col_indices]
linearized = triangle.ravel()
closest_points = np.argsort(linearized)
rows, columns = row_indices[closest_points], col_indices[closest_points]
closest_couples = zip(rows, columns)

boxes = []
for idx, couple in enumerate(closest_couples):
    (p1, p2) = map(int, couple)
    existing_box_idx = [idx for idx, box in enumerate(boxes) if p1 in box or p2 in box]
    if len(existing_box_idx) == 0:
        boxes.append(set([p1, p2]))
    elif len(existing_box_idx) == 1:
        boxes[existing_box_idx[0]].add(p1)
        boxes[existing_box_idx[0]].add(p2)
    else:
        boxes[existing_box_idx[0]] = boxes[existing_box_idx[0]].union(
            boxes[existing_box_idx[1]]
        )
        boxes.pop(existing_box_idx[1])
    if len(boxes[0]) == len(coords):
        print(idx, coords[p1][0] * coords[p2][0])
        break
