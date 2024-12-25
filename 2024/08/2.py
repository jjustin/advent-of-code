#!/usr/bin/env python
import functools as ft
import itertools as it
import os
import subprocess
from collections import defaultdict
from email.policy import default

import numpy as np
from parse import *

try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()
    res = 0

    lines = input.split("\n")
    h = len(lines)
    w = len(lines[0])
    data = defaultdict(list)
    for i, line in enumerate(lines):
        if line == "":
            continue
        for j, char in enumerate(line):
            if char == ".":
                continue
            data[char].append((j, i))

    interferences = set()
    for antenna_type in data:
        for (x1, y1), (x2, y2) in it.combinations(data[antenna_type], 2):
            xdiff = x2 - x1
            ydiff = y2 - y1
            for xcurr, ycurr, f in [
                (x1, y1, lambda x, y: (x - xdiff, y - ydiff)),
                (x2, y2, lambda x, y: (x + xdiff, y + ydiff)),
            ]:
                while True:
                    if xcurr >= 0 and xcurr < w:
                        if ycurr >= 0 and ycurr < h:
                            interferences.add((xcurr, ycurr))
                        else:
                            break
                    else:
                        break
                    xcurr, ycurr = f(xcurr, ycurr)

    res = len(interferences)
    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))