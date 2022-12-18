import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
from collections import defaultdict
from parse import *
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()

    g = set()

    for line in input.split("\n"):
        x, y, z = map(int, line.split(","))
        g.add((x, y, z))

    res = 0
    for x, y, z in g:
        res += sum([1 for i in [-1, 1] if (x + i, y, z) not in g])
        res += sum([1 for i in [-1, 1] if (x, y + i, z) not in g])
        res += sum([1 for i in [-1, 1] if (x, y, z + i) not in g])

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(str(out))
