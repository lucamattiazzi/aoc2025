with open("./day4/input1.txt") as f:
    matrix = f.read().splitlines()

matrix = [list(row) for row in matrix]
row_length = len(matrix[0])
padded_matrix = [
    ["."] * (row_length + 2),
    *[[".", *row, "."] for row in matrix],
    ["."] * (row_length + 2),
]


total_available = 0


def check_available_spots(matrix, coords):
    moves = [(-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1)]
    available_spots = 0
    for move in moves:
        row = coords[0] + move[0]
        column = coords[1] + move[1]
        value = matrix[row][column]
        if value != "@":
            available_spots += 1
    return available_spots


for row_idx in range(1, len(padded_matrix) - 1):
    row = padded_matrix[row_idx]
    for column_idx in range(1, len(row) - 1):
        item = row[column_idx]
        if item != "@":
            continue
        available_spots = check_available_spots(padded_matrix, (row_idx, column_idx))
        if available_spots > 4:
            total_available += 1
            matrix[row_idx - 1][column_idx - 1] = "x"

print(total_available)
