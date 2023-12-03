#!/usr/bin/env python
import functools as ft
import itertools as it
import os
import subprocess
from collections import defaultdict
from curses.ascii import isdigit

import numpy as np
from parse import *

try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()
    res = 0

    data = []
    for line in input.split("\n"):
        data.append([".", *line, "."])
    data = [["."] * len(data[0])] + data + [["."] * len(data[0])]

    for i, line in enumerate(data[1:-1], 1):
        if i == len(data):
            break
        for j, char in enumerate(data[i][1:-1], 1):
            if j == len(data):
                break
            if char != "*":
                continue
            gear_numbers = []
            used_pos = []

            for diff in [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]:
                pos = (i + diff[0], j + diff[1])
                if pos in used_pos:
                    continue

                if data[pos[0]][pos[1]].isdigit():
                    num = 0
                    origin_pos = pos
                    factor = 1
                    while data[pos[0]][pos[1]].isdigit():
                        used_pos.append(pos)
                        num = num + factor * int(data[pos[0]][pos[1]])
                        factor *= 10
                        pos = (pos[0], pos[1] - 1)

                    pos = (origin_pos[0], origin_pos[1] + 1)
                    while data[pos[0]][pos[1]].isdigit():
                        num = 10 * num + int(data[pos[0]][pos[1]])
                        used_pos.append(pos)
                        pos = (pos[0], pos[1] + 1)

                    gear_numbers.append(num)
            if len(gear_numbers) == 2:
                res += gear_numbers[0] * gear_numbers[1]

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
