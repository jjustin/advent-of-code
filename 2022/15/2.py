import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
from parse import *
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str, search_area=4000000):
    input = input.strip()
    m = []
    for line in input.split('\n'):
        if line == "":
            continue

        x, y, bx, by = as_int(
            parse("Sensor at x={}, y={}: closest beacon is at x={}, y={}", line))

        m.append((x, y, abs(x - bx) + abs(y - by)))

    for x, y, d in m:
        i, j = x, y-d-1

        for _ in range(4*(d+1)):
            if all(abs(i - x1) + abs(j - y1) > d for x1, y1, d in m) and i >= 0 and j >= 0 and i < search_area and j < search_area:
                return i * 4000000 + j

            if i >= x and j < y:
                i, j = i+1, j+1
            elif i > x and j >= y:
                i, j = i-1, j+1
            elif i <= x and j > y:
                i, j = i-1, j-1
            elif i < x and j <= y:
                i, j = i+1, j-1

    return 0


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(str(out))
