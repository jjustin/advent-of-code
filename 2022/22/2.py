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


def solve(input: str, side_size=50):
    input_map, input_path = input.split('\n\n')
    input_map = input_map.split('\n')
    tiles = {(i, j): x for j, line in enumerate(input_map)
             for i, x in enumerate(line) if x in ["#", "."]}

    pos = (min(i for (i, j) in tiles if j == 0), 0)
    input_path = input_path.strip()
    input_path = input_path.replace("R", " R ").replace("L", " L ").split(" ")

    facings = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    facing = 0
    seen = []
    for step in input_path:
        if not step.isdigit():
            if step == "R":
                facing = (facing + 1) % 4
            elif step == "L":
                facing = (facing - 1) % 4
            continue

        step = int(step)
        for i in range(step):
            d = facings[facing]
            prev_pos = pos
            prev_facing = facing
            pos = (pos[0] + d[0], pos[1] + d[1])

            if pos not in tiles:
                x, y, facing = wrap(prev_pos, prev_facing, side_size)
                pos = (x, y)
                assert pos in tiles

            if tiles[pos] == "#":
                pos = prev_pos
                facing = prev_facing
                break
            assert tiles[pos] == "."
            seen.append(pos)

    return 1000 * (pos[1]+1) + 4 * (pos[0]+1) + facing


def wrap(prev_pos, facing, side_size):
    yprev = prev_pos[1]
    xprev = prev_pos[0]
    x_side = prev_pos[0]//side_size
    y_side = prev_pos[1]//side_size
    x = -1
    y = -1

    # print(f"Before wrap facing {facing}, x:{x_side}, y:{y_side}", end="")

    assert y_side in [0, 1, 2, 3]
    assert x_side in [0, 1, 2]
    if facing == 0:
        if y_side == 0:
            facing = 2
            x = 2*side_size - 1
            y = 3*side_size - 1 - yprev
        elif y_side == 1:
            facing = 3
            x = 2*side_size + yprev - side_size
            y = side_size - 1
        elif y_side == 2:
            facing = 2
            x = 3*side_size - 1
            y = side_size - 1 - (yprev - 2*side_size)
        elif y_side == 3:
            facing = 3
            x = side_size + (yprev - 3*side_size)
            y = 3*side_size - 1

    elif facing == 1:
        if x_side == 0:
            facing = 1
            x = xprev + 2*side_size
            y = 0
        if x_side == 1:
            facing = 2
            x = side_size - 1
            y = 3*side_size + (xprev - side_size)
        if x_side == 2:
            facing = 2
            x = 2*side_size - 1
            y = side_size + (xprev - 2*side_size)

    elif facing == 2:
        if y_side == 0:
            facing = 0
            x = 0
            y = 3*side_size - 1 - yprev
        if y_side == 1:
            facing = 1
            x = yprev - side_size
            y = 2*side_size
        if y_side == 2:
            facing = 0
            x = side_size
            y = side_size - 1 - (yprev - 2*side_size)
        if y_side == 3:
            facing = 1
            x = side_size + (yprev - 3*side_size)
            y = 0

    elif facing == 3:
        if x_side == 0:
            facing = 0
            x = side_size
            y = side_size + xprev
        if x_side == 1:
            facing = 0
            x = 0
            y = 3*side_size + xprev - side_size
        if x_side == 2:
            facing = 3
            x = xprev - 2*side_size
            y = 4*side_size - 1
    #print(f" wrap around: {prev_pos} -> {(x,y)}")
    return x, y, facing


def test_wrap():
    """
    ensure that wrap around works
    """
    def xright(y):
        if y in [0, 1]:
            return 5
        if y in [2, 3, 4, 5]:
            return 3
        if y in [6, 7]:
            return 1
        print("y", y)
        assert False

    def ydown(x):
        if x in [0, 1]:
            return 7
        if x in [2, 3]:
            return 5
        if x in [4, 5]:
            return 1
        print("x", x)
        assert False

    def xleft(y):
        if y in [0, 1, 2, 3]:
            return 2
        if y in [4, 5, 6, 7]:
            return 0
        print("y", y)
        assert False

    def yup(x):
        if x in [2, 3, 4, 5]:
            return 0
        if x in [0, 1]:
            return 4
        print("x", x)
        assert False

    test_cases = [
        (0, (xright(y), y)) for y in range(8)
    ] + [
        (1, (x, ydown(x))) for x in range(6)
    ] + [
        (2, (xleft(y), y)) for y in range(8)
    ] + [
        (3, (x, yup(x))) for x in range(6)
    ]
    grid = {pos: "." for _, pos in test_cases}

    for facing, (x, y) in test_cases:
        x2, y2, facing2 = wrap((x, y), facing, 2)
        # wrapped point must be in grid
        assert (x, y) in grid
        facing2 = (facing2 + 2) % 4  # turn around
        x2, y2, facing2 = wrap((x2, y2), facing2, 2)
        facing2 = (facing2 + 2) % 4  # turn around
        # we should be back at starting point
        assert (x, y) == (x2, y2)
        assert facing == facing2


def printmap(map, seen):
    max_i = max(i for i, j in map)
    max_j = max(j for i, j in map)

    for j in range(max_j + 1):
        for i in range(max_i + 1):
            if (i, j) in seen:
                print("*", end="")
            elif (i, j) not in map:
                print(" ", end="")
            else:
                print(map[(i, j)], end="")
        print()


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


test_wrap()


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
