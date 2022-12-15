import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
import parse
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()
    grid = {}
    for line in input.split('\n'):
        x, y = -1, -1

        if line == "":
            continue
        for move in line.split(" -> "):
            if x == -1 and y == -1:
                x, y = map(int, move.split(","))
                continue

            x_end, y_end = map(int, move.split(","))

            dx = 1 if x < x_end else -1
            dy = 1 if y < y_end else -1
            for x in range(x, x_end + dx, dx):
                for y in range(y, y_end + dy, dy):
                    grid[(x, y)] = "#"

    y_lim = max([y for x, y in grid])
    while 1:
        sand = (500, 0)

        if sand in grid:
            break
        while 1:
            if sand[1] >= y_lim:
                # print_grid(grid)
                return sum([1 for x, y in grid if grid[(x, y)] == 'o'])

            cont = False
            for sand_new in [tuple_sum(sand, (0, 1)), tuple_sum(sand, (-1, 1)), tuple_sum(sand, (1, 1))]:
                if sand_new not in grid:
                    sand = sand_new
                    cont = True
                    break

            if cont:
                continue
            break
        grid[sand] = 'o'

    return -1


def print_grid(grid):
    for y in range(0, tuple_max(grid, 1)+2):
        for x in range(tuple_min(grid, 0)-1, tuple_max(grid, 0)+2):
            print(grid[(x, y)] if (x, y) in grid else ".", end="")
        print()


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
