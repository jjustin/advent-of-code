#!/usr/bin/env python
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
    res = 0

    data = []
    write_disk = True
    disk_id = 0
    for n in [int(x) for x in input]:
        c = None
        if write_disk:
            c = disk_id
        data += [c] * n
        if write_disk:
            disk_id += 1
        write_disk = not write_disk

    left = 0
    right = len(data) - 1
    while left < right:
        if data[left] is None:
            data[left] = data[right]
            data[right] = None
            right -= 1
            while data[right] is None:
                right -= 1
        left += 1

    for i, n in enumerate(data):
        if n is not None:
            res += i * n

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
