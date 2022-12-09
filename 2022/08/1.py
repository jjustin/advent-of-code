import itertools as it
import os
import numpy as np


def handle_result(result):
    print(result)


def solve(input: str):
    grid = []
    for i, line in enumerate(input.split('\n')):
        if line == "":
            continue
        grid.append([int(c) for c in line])
    grid = np.array(grid)

    visible = 4 * len(grid) - 4
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            h = grid[i, j]

            top = grid[0:i, j]
            left = grid[i, :j]
            bottom = grid[i+1:, j]
            right = grid[i, j+1:]

            visible_from_any_side = any([h > max(
                possible_obstructions) for possible_obstructions in [top, left, bottom, right]])

            if visible_from_any_side:
                visible += 1

    return visible


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(out)
