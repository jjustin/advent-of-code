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

    for line in input.split("\n"):
        if line == "":
            continue

        safe_outer = False
        for type in ["normal", "skip_first", "skip_second"]:
            desc = False
            safe = True
            prev = 1
            levels = line.split()
            if type == "normal":
                one_bad = False
            if type == "skip_first":
                one_bad = True
                levels = levels[1:]
            if type == "skip_second":
                one_bad = True
                levels = levels[:1] + levels[2:]

            for i, level_str in enumerate(levels):
                level = int(level_str)

                if i == 1:
                    if prev > level:
                        desc = True

                if i == 0:
                    prev = level
                    continue

                diff = prev - level
                this_bad = False
                if desc:
                    if diff > 3 or diff < 1:
                        if not one_bad:
                            one_bad = True
                            this_bad = True
                        else:
                            safe = False
                            break
                else:
                    if diff < -3 or diff > -1:
                        if not one_bad:
                            one_bad = True
                            this_bad = True
                        else:
                            safe = False
                            break

                if not this_bad:
                    prev = level

            if safe:
                safe_outer = True
                break

        if safe_outer:
            res += 1

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
