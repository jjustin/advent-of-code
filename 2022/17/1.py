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
    nm = gen_input(input)

    def next_move():
        return next(nm)

    g = {(i, 0) for i in range(7)}
    for i in range(2022):
        x, y = 2, max(y for x, y in g) + 4
        rock = rocks[i % 5]

        while True:
            dx = 1 if next_move() == ">" else -1

            if all((x + i + dx, y + j) not in g and 0 <= x + i + dx < 7
                    for i, j in rock):
                x += dx

            if any((x + i, y + j - 1) in g for i, j in rock):
                break

            y -= 1

        g.update((x + i, y + j) for i, j in rocks[i % 5])

    return max(y for x, y in g)


def gen_input(input):
    while 1:
        for c in input:
            yield c


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

sample_input = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
sample_res = 3068

sample_out = solve(sample_input)
print(sample_out)
if sample_out != sample_res:
    print("Sample incorrect!!")
    exit()


out = solve(input)
handle_result(str(out))
