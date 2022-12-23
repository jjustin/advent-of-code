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
        d = facings[facing]
        for i in range(step):
            prev_pos = pos
            pos = (pos[0] + d[0], pos[1] + d[1])

            if pos not in tiles:
                # wrap around
                if facing == 0:
                    # right
                    m = min(i for (i, j) in tiles if j == pos[1])
                    pos = (m, pos[1])
                elif facing == 1:
                    # down
                    m = min(j for (i, j) in tiles if i == pos[0])
                    pos = (pos[0], m)
                elif facing == 2:
                    # left
                    m = max(i for (i, j) in tiles if j == pos[1])
                    pos = (m, pos[1])
                elif facing == 3:
                    # up
                    m = max(j for (i, j) in tiles if i == pos[0])
                    pos = (pos[0], m)

            if tiles[pos] == "#":
                pos = prev_pos
                break
            assert tiles[pos] == "."
            seen.append(pos)

    return 1000 * (pos[1]+1) + 4 * (pos[0]+1) + facing


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


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

sample_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

sample_res = 6032

sample_out = solve(sample_input)
print(sample_out)
if sample_out != sample_res:
    print("Sample incorrect!!")
    exit()


out = solve(input)
handle_result(str(out))
