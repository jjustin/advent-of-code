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

    tiles = {(i, j) for j, line in enumerate(input.split("\n"))
             for i, x in enumerate(line) if x in ["#"] and line != ""}

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for round in range(10):
        new_tiles = {}
        for (x, y) in tiles:
            alone = True
            for dx, dy in it.product([-1, 0, 1], [-1, 0, 1]):
                if dx == 0 and dy == 0:
                    continue
                if (x+dx, y+dy) in tiles:
                    alone = False
                    break
            if alone:
                continue

            for (dx, dy) in directions:
                if dx == 0:
                    check_dx = {1, 0, -1}
                    check_dy = {dy}
                elif dy == 0:
                    check_dy = {1, 0, -1}
                    check_dx = {dx}

                empty = True
                for (ndx, ndy) in it.product(check_dx, check_dy):
                    if (x + ndx, y + ndy) in tiles:
                        empty = False
                        break

                if empty:
                    new_pos = (x + dx, y + dy)
                    if new_pos not in new_tiles:
                        new_tiles[new_pos] = []
                    new_tiles[new_pos].append((x, y))
                    break

        for move_to, move_from in new_tiles.items():
            if len(move_from) == 1:
                tiles.remove(move_from[0])
                tiles.add(move_to)

        directions = directions[1:] + [directions[0]]

    minx = min(x for x, y in tiles)
    maxx = max(x for x, y in tiles)
    miny = min(y for x, y in tiles)
    maxy = max(y for x, y in tiles)
    return (maxx - minx + 1) * (maxy - miny + 1) - len(tiles)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
