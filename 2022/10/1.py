import itertools as it
import os
import subprocess
import functools
import numpy as np


def solve(input: str):
    X = 1
    tick = 1
    interesting_ticks = [20, 60, 100, 140, 180, 220]
    signal_strengths = []

    for line in input.split('\n'):
        if line == "":
            continue

        prev_X = X

        if line.startswith("addx"):
            X += int(line[5:])
            tick += 2
        elif line.startswith("noop"):
            tick += 1

        if len(interesting_ticks) > 0 and tick >= interesting_ticks[0]:
            t = interesting_ticks.pop(0)

            if tick == t:
                signal_strengths.append(t * X)
            elif tick > t:
                signal_strengths.append(t * prev_X)

    return sum(signal_strengths)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(str(out))
