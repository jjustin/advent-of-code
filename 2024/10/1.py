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

    input = input.split("\n")
    data = []
    h = len(input)
    w = len(input[0])
    for line in input:
        if line == "":
            continue
        data.append([int(x) for x in line])

    for x in range(w):
        for y in range(h):
            if data[y][x] == 0:
                found = check(data, x, y)
                res += len(found)

    return res


def check(data, x, y):
    curr = data[y][x]
    if curr == 9:
        return set([(x, y)])

    out = set()
    if x != 0 and data[y][x - 1] == curr + 1:
        out = out.union(check(data, x - 1, y))
    if y != 0 and data[y - 1][x] == curr + 1:
        out = out.union(check(data, x, y - 1))
    if y != len(data) - 1 and data[y + 1][x] == curr + 1:
        out = out.union(check(data, x, y + 1))
    if x != len(data[0]) - 1 and data[y][x + 1] == curr + 1:
        out = out.union(check(data, x + 1, y))

    return out


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
