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

        if check_possible(expected, numbers):
            res += expected

    return res


def check_possible(exp, l):
    if len(l) == 1:
        return exp == l[0]

    last_value = l[len(l) - 1]
    mid_res = exp - last_value
    if mid_res >= 0:
        if check_possible(mid_res, l[: (len(l) - 1)]):
            return True

    mid_res = float(exp / last_value)
    if mid_res.is_integer():
        if check_possible(int(mid_res), l[: (len(l) - 1)]):
            return True

    if f"{exp}".endswith(f"{last_value}") and exp != last_value:
        mid_res = int(f"{exp}".removesuffix(f"{last_value}"))
        if check_possible(mid_res, l[: (len(l) - 1)]):
            return True


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
