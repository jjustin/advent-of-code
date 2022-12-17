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
    rocks = (
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
        ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
    )

    input = input.strip()
    input_ix = 0

    g = {(i, 0) for i in range(7)}
    mem = {}
    i = 0

    while i < 1000000000000:
        h = max(y for x, y in g)
        x, y = 2,  h + 4
        rock = rocks[i % 5]

        cache_key = [h - max(y for x, y in g if x == i) for i in range(7)]
        cache_key += [input_ix, i % 5]
        cache_key = tuple(cache_key)

        if cache_key in mem:
            (i_under, h_under) = mem[cache_key]
            h_diff = h - h_under
            rocks_between = i - i_under

            # Apply cache once we find a section that can be repeated until our goal is hit
            if ((1000000000000 - i_under) % rocks_between == 0):
                return h_diff * ((1000000000000 - i_under) // rocks_between) + h_under

        mem[cache_key] = (i, h)

        while True:
            dx = 1 if input[input_ix] == ">" else -1
            input_ix = (input_ix + 1) % len(input)

            if all((x + i + dx, y + j) not in g and 0 <= x + i + dx < 7
                    for i, j in rock):
                x += dx

            if any((x + i, y + j - 1) in g for i, j in rock):
                break

            y -= 1

        g.update((x + i, y + j) for i, j in rocks[i % 5])
        i += 1

    return max(y for x, y in g)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
