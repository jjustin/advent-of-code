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

    [i1, i2] = input.split("\n\n")
    states = {}
    for line in i1.split("\n"):
        if line == "":
            continue
        name, val = parse("{}: {}", line)

        if val == "0":
            states[name] = False
        else:
            states[name] = True

    gates = {}
    for line in i2.split("\n"):
        if line == "":
            continue
        x1, op, x2, dest = parse("{} {} {} -> {}", line)
        gates[dest] = (x1, op, x2)

    something_found = True
    while something_found:
        something_found = False
        for dest, (x1, op, x2) in gates.items():
            if dest not in states and x1 in states and x2 in states:
                something_found = True
                if op == "AND":
                    states[dest] = states[x1] and states[x2]
                if op == "OR":
                    states[dest] = states[x1] or states[x2]
                if op == "XOR":
                    states[dest] = states[x1] != states[x2]

    for i in range(50):
        key = f"z{i:02}"
        if key in states and states[key]:
            res += pow(2, i)

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
