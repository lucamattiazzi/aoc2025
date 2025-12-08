from copy import deepcopy

import numpy as np

with open("./day10/input1.txt") as f:
    lines = f.readlines()


def parse_operands(strings: list[str], length: int) -> list[list[int]]:
    operands = []
    for string in strings:
        operand = np.array([0] * length)
        string = string[1:-1].split(",")
        for i in string:
            operand[int(i)] = 1
        operands.append(np.array(operand))
    return operands


def parse_joltages(string: str):
    return np.array(list(map(int, string[1:-1].split(","))))


problems = []

for line in lines:
    line = line.strip().split(" ")

    joltages = line[-1]
    joltages = parse_joltages(joltages)

    operands = line[1:-1]
    operands = parse_operands(operands, len(joltages))

    problem = {
        "operands": operands,
        "final": joltages,
        "current": np.array([0] * len(joltages)),
        "operations": [],
    }
    problems.append(problem)


def get_problem_key(problem):
    return str(problem["current"])


def solve_problem(original_problem):
    for idx, operand in enumerate(original_problem["operands"]):
        problem = deepcopy(original_problem)
        problem["current"] += operand
        problem["operations"].append(idx)
        if np.array_equal(problem["current"], problem["final"]):
            return problem
        if np.any(problem["current"] > problem["final"]):
            continue
        solution = solve_problem(problem)
        if solution is not None:
            return solution
    return


total_moves = 0

for problem in problems:
    solved_problem = solve_problem(problem)
    total_moves += len(solved_problem["operations"])
    print(len(solved_problem["operations"]))
print("total_moves", total_moves)
