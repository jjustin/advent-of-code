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

    for i, line in enumerate(data, 1):
        if i == len(data):
            break
        for j, char in enumerate(data[i], 1):
            if j == len(data):
                break

            if not data[i][j].isdigit():
                continue
            if data[i][j - 1].isdigit():
                continue

            end_j = j
            while data[i][end_j].isdigit():
                end_j += 1

            is_ok = False
            for k in range(j, end_j):
                if is_ok:
                    break
                for diff_x in [-1, 0, 1]:
                    for diff_y in [-1, 0, 1]:
                        if diff_x == 0 and diff_y == 0:
                            continue
                        comp = data[i + diff_x][k + diff_y]

                        if not comp.isdigit() and comp != ".":
                            is_ok = True

            if is_ok:
                v = int("".join(data[i][j:end_j]))
                res += v

    return res


def tuple_sum(*t):
    return tuple(map(sum, zip(*t)))


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
