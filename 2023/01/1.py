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

        first = None
        last = None

        for char in line:
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                if first is None:
                    first = int(char)
                last = int(char)

        if first is not None and last is not None:
            res += 10 * first + last

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
