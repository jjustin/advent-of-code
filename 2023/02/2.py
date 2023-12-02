#!/usr/bin/env python
import functools as ft
import itertools as it
import os
import subprocess
from collections import defaultdict
from operator import is_

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

        [_, cubes] = line.split(":")

        ginfo = defaultdict(lambda: 0)
        for s in cubes.split(";"):
            for pair in s.split(", "):
                x = pair.split(" ")
                ginfo[x[-1]] = max(int(x[-2]), ginfo[x[-1]])

        data.append(ginfo["red"] * ginfo["green"] * ginfo["blue"])

    return sum(data)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
