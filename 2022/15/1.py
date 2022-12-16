import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
from parse import *
try:
    from utils import *
except ImportError:
    print("No utils found, not importing")


def solve(input: str, look_at_y=2000000):
    input = input.strip()
    beacons_overlapping = []
    not_at = set()
    for line in input.split('\n'):
        if line == "":
            continue

        x, y, bx, by = as_int(
            parse("Sensor at x={}, y={}: closest beacon is at x={}, y={}", line))

        if by == look_at_y:
            beacons_overlapping.append(by)

        diff = abs(x - bx) + abs(y - by)
        dy = abs(y - look_at_y) - 1

        r = diff - dy - 1
        for a in range(x - r, x + r + 1):
            not_at.add(a)

    for i in beacons_overlapping:
        not_at.discard(i)

    return len(not_at)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
