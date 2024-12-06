#!/usr/bin/env python
import functools as ft
import itertools as it
import os
import subprocess
from collections import defaultdict

import numpy as np
from parse import *

try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()
    res = 0

    map_data = {}
    start_pos = (0, 0)
    h = len(input.split("\n"))
    w = len(input.split("\n")[0])
    for y, line in enumerate(input.split("\n")):
        if line == "":
            continue
        for x, char in enumerate(line):
            if char == "#":
                map_data[(x, y)] = True
            if char == "^":
                start_pos = (x, y)

    default_visited = None
    for x in range(-1, w):
        print(f"{x}/{w}")
        for y in range(-1, h):
            if (x, y) in map_data or (x, y) == start_pos:
                continue

            if x == -1 and y == -1 and default_visited is not None:
                # Only run he default path once
                continue

            if default_visited is not None and (x, y) not in default_visited:
                # Skip if obstacle is not on watcher's path
                continue

            map_data[(x, y)] = True

            current_pos = start_pos
            direction = (0, -1)
            visited = {}
            while h > current_pos[0] >= 0 and w > current_pos[1] >= 0:
                if (current_pos, direction) in visited:
                    res += 1
                    break
                visited[(current_pos, direction)] = True
                next_pos = (
                    current_pos[0] + direction[0],
                    current_pos[1] + direction[1],
                )
                if next_pos in map_data:
                    direction = (-direction[1], direction[0])
                    continue
                current_pos = next_pos

            if x == -1 and y == -1:
                # Store the path with no extra obstacles
                default_visited = [v[0] for v in visited]

            del map_data[(x, y)]

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
