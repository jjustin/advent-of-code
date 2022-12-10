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
    head = (0, 0)
    tail = (0, 0)
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

        for i in range(num):
            head_old = head
            head = tuple(map(sum, zip(head, moves[way])))

            if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                tail = head_old

            tails.add(tail)

    return len(tails)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(str(out))
