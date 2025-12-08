from copy import deepcopy

import numpy as np

with open("./day10/input1.txt") as f:
    lines = f.readlines()


def parse_solution(string: str) -> list[int]:
    value_map = {".": 1, "#": -1}
    return np.array([value_map[k] for k in string[1:-1]])


def parse_operands(strings: list[str], length: int) -> list[list[int]]:
    operands = []
    for string in strings:
        operand = [1] * length
        string = string[1:-1].split(",")
        for i in string:
            operand[int(i)] = -1
        operands.append(np.array(operand))
    return operands


problems = []

for line in lines:
    line = line.strip().split(" ")

    solution = line.pop(0)
    solution = parse_solution(solution)

    base = np.array([1] * len(solution))

    operands = line[:-1]
    operands = parse_operands(operands, len(solution))
    problem = {
        "current": base,
        "solution": solution,
        "operands": operands,
        "operations": [],
    }
    problems.append(problem)


def get_problem_key(problem):
    return str(problem["current"])


def solve_problem(problem):
    states = {get_problem_key(problem): problem}
    while True:
        new_states = {}
        for state in states.values():
            for operand in state["operands"]:
                current_state = deepcopy(state)
                current_state["current"] = current_state["current"] * operand
                current_key = get_problem_key(current_state)
                if current_key in states:
                    continue
                current_state["operations"].append(operand)
                if np.array_equal(current_state["current"], current_state["solution"]):
                    return current_state
                new_states[current_key] = current_state
        states = {**states, **new_states}


total_moves = 0

for problem in problems:
    solved_problem = solve_problem(problem)
    total_moves += len(solved_problem["operations"])
    print(len(solved_problem["operations"]))
print("total_moves", total_moves)
