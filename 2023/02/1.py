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

    data = []
    for line in input.split("\n"):
        if line == "":
            continue

        [game, cubes] = line.split(":")
        [_, gid] = game.split(" ")

        is_ok = True

        for s in cubes.split(";"):
            ginfo = defaultdict(lambda: 0)

            for pair in s.split(", "):
                x = pair.split(" ")
                ginfo[x[-1]] += int(x[-2])

            if ginfo["red"] > 12 or ginfo["green"] > 13 or ginfo["blue"] > 14:
                is_ok = False

        if is_ok:
            data.append(int(gid))

    return sum(data)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
