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

    rules = []
    sections = input.split("\n\n")
    for line in sections[0].split("\n"):
        x = line.split("|")
        rules.append((int(x[0]), int(x[1])))

    for line in sections[1].split("\n"):
        numbers = list(map(int, line.split(",")))
        mapped = {}
        for i, number in enumerate(numbers):
            mapped[number] = i

        breaks = False
        for first, second in rules:
            if first in mapped and second in mapped:
                if mapped[first] > mapped[second]:
                    breaks = True
            if breaks:
                break
        if not breaks:
            res += numbers[len(numbers) // 2]

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
