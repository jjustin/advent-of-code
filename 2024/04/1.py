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

    data = []
    for line in input.split("\n"):
        if line == "":
            continue

        data.append(list(line))

    for y in range(len(data)):
        for x in range(len(data[0])):
            for x_diff in [-1, 0, 1]:
                for y_diff in [-1, 0, 1]:
                    if x_diff == 0 and y_diff == 0:
                        continue
                    res += find_xmas(data, x, y, x_diff, y_diff, "")

    return res


def find_xmas(l, x, y, x_diff, y_diff, so_far):
    if len(so_far) == 4:
        if so_far == "XMAS":
            return 1
        return 0

    if x < 0 or y < 0 or x >= len(l[0]) or y >= len(l):
        return 0

    so_far += l[y][x]
    x = x + x_diff
    y = y + y_diff

    return find_xmas(l, x, y, x_diff, y_diff, so_far)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
