import itertools as it
import os
import subprocess
import functools
import numpy as np


def solve(input: str):
    X = 1
    tick = 1

    for line in input.split('\n'):
        if line == "":
            continue

        if line.startswith("addx"):
            tick += 1
            draw(tick, X)
            X += int(line[5:])
            tick += 1
            draw(tick, X)
        elif line.startswith("noop"):
            tick += 1
            draw(tick, X)

    return


def draw(tick, X):
    res = ""
    x_pos = (tick-1) % 40

    if x_pos in range(X-1, X+2):
        res += "#"
    else:
        res += "."
    print(res, end="")

    if x_pos == 39:
        print()


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
# handle_result(str(out))
