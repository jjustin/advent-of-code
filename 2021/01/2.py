import functools as ft
import itertools as it
import os
import subprocess
from collections import defaultdict

import numpy as np

from parse import *

try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()
    res = -1

    data = []
    for line in input.split("\n"):
        if line == "":
            continue
        data.append(int(line))

    data = np.convolve(data, np.ones(3), mode="valid")

    prev = 0
    print(data)
    for line in data:
        if int(line) > prev:
            print(line)
            res += 1
        prev = int(line)

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
