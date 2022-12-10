import itertools as it
import os
import subprocess
import functools
import numpy as np
try:
    from utils import *
except ImportError:
    pass


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


def solve(input: str):
    rope = [(0, 0)] * 10
    tails = set()

    moves = {
        "U": (0, 1),
        "R": (1, 0),
        "D": (0, -1),
        "L": (-1, 0),
    }

    for line in input.split('\n'):
        if line == "":
            continue

        [way, num] = line.split(" ")
        num = int(num)

        for _ in range(num):
            rope[0] = tuple_sum(rope[0], moves[way])

            for i in range(1, len(rope)):
                diff = tuple_diff(rope[i], rope[i-1])
                dx, dy = diff

                if abs(dx) > 1 or abs(dy) > 1:
                    cx, cy = 0, 0
                    if dx != 0:
                        cx = -dx if abs(dx) == 1 else -dx//2
                    if dy != 0:
                        cy = -dy if abs(dy) == 1 else -dy//2
                    rope[i] = tuple_sum(rope[i], (cx, cy))

            tails.add(rope[-1])

    return len(tails)


def tuple_sum(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


def tuple_diff(t1, t2):
    return tuple(map(lambda a: a[0]-a[1], zip(t1, t2)))


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(str(out))
