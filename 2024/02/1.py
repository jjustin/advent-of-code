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
        
        prev = 0
        desc = False
        safe = True
        for (i, level_str) in enumerate(line.split()):
            level = int(level_str)

            if i == 1:
                if prev > level:
                    desc = True

            if i == 0:
                prev = level
                continue

            diff = prev - level
            if desc:
                if diff > 3 or diff < 1:
                    safe = False
                    break
            else:
                if diff < -3 or diff > -1:
                    safe = False
                    break
            
            prev = level

        if safe:
            res += 1


    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
