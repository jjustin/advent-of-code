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

    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            res += find_xmas(data, x, y)

    return res


def find_xmas(l, x, y):
    if l[y][x] != "A":
        return 0

    left_up = l[y - 1][x - 1]
    left_down = l[y + 1][x - 1]
    right_down = l[y + 1][x + 1]
    right_up = l[y - 1][x + 1]

    if (left_up == left_down and right_down == right_up) or (
        left_up == right_up and left_down == right_down
    ):
        if (left_up == "S" and right_down == "M") or (
            left_up == "M" and right_down == "S"
        ):
            return 1
    return 0


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
