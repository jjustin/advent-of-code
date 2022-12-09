import itertools as it
import os
import numpy as np
from functools import reduce


def handle_result(result):
    print(result)


def solve(input: str):
    grid = []
    for i, line in enumerate(input.split('\n')):
        if line == "":
            continue
        grid.append([int(c) for c in line])
    grid = np.array(grid)

    visible_best = -1
    for i in range(len(grid)):
        for j in range(len(grid)):
            h = grid[i, j]

            top = grid[0:i, j][::-1]
            left = grid[i, :j][::-1]
            bottom = grid[i+1:, j]
            right = grid[i, j+1:]

            higher_counts = [higher_count(h, view)
                             for view in [top, left, bottom, right]]
            visible = reduce(lambda x, y: x*y, higher_counts)

            visible_best = max(visible_best, visible)

    return visible_best


def higher_count(h, view):
    if len(view) == 0:
        return 0
    if all(view < h):
        return len(view)
    return np.argmax(view >= h)+1


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(out)
