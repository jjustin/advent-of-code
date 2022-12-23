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

# This solution works for sample input, but not for the actual input. The cube map in different and consequently, the mapping between cube sides is different.


def solve(input: str, side_size=50):
    input_map, input_path = input.split('\n\n')
    input_map = input_map.split('\n')
    tiles = {(i, j): x for j, line in enumerate(input_map)
             for i, x in enumerate(line) if x in ["#", "."]}
    # printmap(map, set())

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
                x_side = prev_pos[0]//side_size
                y_side = prev_pos[1]//side_size

                assert y_side in [0, 1, 2]
                assert x_side in [0, 1, 2, 3]
                x = -1
                y = -1
                print(
                    f"Before wrap facing {facing}, x:{x_side}, y:{y_side}", end="")
                # wrap around
                if facing == 0:
                    if y_side == 0:
                        facing = 2
                        x = (4*side_size) - 1,
                        y = (3*side_size) - prev_pos[1] - 1
                    if y_side == 1:
                        facing = 1
                        x = 4*side_size - 1 - (prev_pos[1] - side_size)
                        y = 2*side_size
                    if y_side == 2:
                        facing = 2
                        x = 3*side_size - 1
                        y = 3*side_size - prev_pos[1] - 1

                elif facing == 1:
                    if x_side == 0:
                        facing = 3
                        x = 3*side_size - prev_pos[0] - 1
                        y = 3*side_size - 1
                    if x_side == 1:
                        facing = 0
                        x = 2*side_size
                        y = 3*side_size - 1 - (prev_pos[0] - side_size)
                    if x_side == 2:
                        facing = 3
                        x = 3*side_size - prev_pos[0] - 1
                        y = 2*side_size - 1
                    if x_side == 3:
                        facing = 0
                        x = 0
                        y = 2*side_size - 1 - (prev_pos[0] - 3*side_size)

                elif facing == 2:
                    if y_side == 0:
                        facing = 1
                        x = side_size + prev_pos[1]
                        y = side_size
                    if y_side == 1:
                        facing = 3
                        x = 4*side_size - (prev_pos[1] - side_size) - 1
                        y = 3*side_size - 1
                    if y_side == 2:
                        facing = 0
                        x = 2*side_size - (prev_pos[1] - 2*side_size) - 1
                        y = 2*side_size - 1

                elif facing == 3:
                    if x_side == 0:
                        facing = 1
                        x = 3 * side_size - 1 - prev_pos[0]
                        y = 0
                    if x_side == 1:
                        facing = 0
                        x = 2 * side_size
                        y = prev_pos[0] - side_size
                    if x_side == 2:
                        facing = 1
                        x = side_size - 1 - (prev_pos[0] - 2*side_size)
                        y = side_size
                    if x_side == 3:
                        facing = 0
                        x = 3*side_size - 1
                        y = 2*side_size - 1 - (prev_pos[0] - 3*side_size)

                pos = (x, y)
                print(
                    f" wrap around: {prev_pos} -> {pos}")
                assert pos in tiles

            if tiles[pos] == "#":
                pos = prev_pos
                facing = prev_facing
                break
            assert tiles[pos] == "."
            seen.append(pos)
    # printmap(tiles, seen)
    print(pos, facing)
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

sample_res = 5031

sample_out = solve(sample_input, 4)
print(sample_out)
if sample_out != sample_res:
    print("Sample incorrect!!")
    exit()
