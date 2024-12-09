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
        data.append((c, n))
        if write_disk:
            disk_id += 1
        write_disk = not write_disk

    for to_move in list(reversed(list(data))):
        j = data.index(to_move)
        (v, l) = to_move
        if v is None:
            continue

        for i, (x, free) in enumerate(data):
            if i > j:
                break
            if x is not None:
                continue
            if free >= l:
                add = [to_move]
                if free != l:
                    add.append((None, free - l))
                data = data[:i] + add + data[i + 1 : j] + [(None, l)] + data[j + 1 :]
                break

    i = 0
    for n, c in data:
        if n is None:
            i += c
        else:
            for j in range(c):
                res += i * n
                i += 1

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
