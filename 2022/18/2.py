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

    minp = tuple(min(a[i] - 1 for a in g) for i in range(3))
    maxp = tuple(max(a[i] + 1 for a in g) for i in range(3))

    seen = set()
    todo = {minp}

    res = 0
    while todo:
        p = todo.pop()

        if p in seen:
            continue
        seen.add(p)

        for d in range(3):
            for s in (-1, 1):
                np = tuple(p[i] + s if i == d else p[i] for i in range(3))
                if np in g:
                    res += 1
                elif np not in todo and all(minp[i] <= np[i] <= maxp[i] for i in range(3)):
                    todo.add(np)

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
