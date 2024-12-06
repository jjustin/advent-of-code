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
    current_pos = (0, 0)
    direction = (0, -1)
    h = len(input.split("\n"))
    w = len(input.split("\n")[0])
    for y, line in enumerate(input.split("\n")):
        if line == "":
            continue
        for x, char in enumerate(line):
            if char == "#":
                map_data[(x, y)] = True
            if char == "^":
                current_pos = (x, y)

    visited = {}
    while h > current_pos[0] >= 0 and w > current_pos[1] >= 0:
        visited[current_pos] = True
        next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
        if next_pos in map_data:
            direction = (-direction[1], direction[0])
            continue
        current_pos = next_pos

    res += len(visited)
    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
