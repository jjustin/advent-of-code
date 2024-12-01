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

    left = []
    right = []

    for line in input.split("\n"):
        if line == "":
            continue
        x = line.split()
        left.append(int(x[0]))
        right.append(int(x[1]))

    l = np.sort(left)
    r = np.sort(right)

    res = np.sum(np.abs(l - r))

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
