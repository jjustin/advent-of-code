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

        [expected, numbers] = line.split(": ")
        expected = int(expected)
        numbers = [int(x) for x in numbers.split(" ")]

        if check_possible(expected, numbers, numbers[0], 1):
            res += expected

    return res


def check_possible(exp, l, current, ix):
    if ix == len(l):
        return current == exp

    if current > exp:
        return False

    if check_possible(exp, l, current + l[ix], ix + 1):
        return True
    if check_possible(exp, l, current * l[ix], ix + 1):
        return True
    if check_possible(exp, l, int(f"{current}{l[ix]}"), ix + 1):
        return True


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
