import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
from collections import defaultdict
from parse import *
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()
    grid = {(x, y): [c] for y, line in enumerate(input.split('\n'))
            for x, c in enumerate(line) if c != '.'}
    w, h = (len(input.split('\n')[0]), len(input.split('\n')))

    moves = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1), " ": (0, 0)}

    def navigate(grid, pos, end):
        for i in range(10000):
            new_grid = {}
            for el in grid:
                if grid[el] == ['#']:
                    new_grid[el] = ['#']
                    continue
                for blizzard in grid[el]:
                    x, y = el
                    move = moves[blizzard]

                    n = (x + move[0], y + move[1])
                    if n in grid and grid[n] == ['#']:
                        if blizzard == '>':
                            n = (1, y)
                        elif blizzard == '<':
                            n = (w - 2, y)
                        elif blizzard == '^':
                            n = (x, h-2)
                        elif blizzard == 'v':
                            n = (x, 1)
                    if n not in new_grid:
                        new_grid[n] = []
                    new_grid[n].append(blizzard)

            grid = new_grid

            new_pos = set()
            for el in pos:
                for move in moves.values():
                    n = (el[0] + move[0], el[1] + move[1])
                    if n[0] < 0 or n[1] < 0 or n[0] >= w or n[1] >= h:
                        continue
                    if n not in new_grid:
                        new_pos.add(n)
            pos = new_pos
            if end in pos:
                return i + 1, grid

    start = (1, 0)
    end = (w-2, h-1)
    x1, grid = navigate(grid, {start}, end)
    x2, grid = navigate(grid, {end}, start)
    x3, grid = navigate(grid, {start}, end)

    return x1+x2+x3


def printmap(grid, pos):
    maxx = max(x for x, y in grid.keys())
    maxy = max(y for x, y in grid.keys())
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if (x, y) in pos:
                print('E', end='')
            else:
                n = grid.get((x, y), ['.'])
                if len(n) == 1:
                    print(n[0], end='')
                else:
                    print(len(n), end='')
        print()


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(str(out))
