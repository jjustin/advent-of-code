import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
from collections import defaultdict
from parse import *
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()
    res = "no result provided"
    orig_vals = {}

    for line in input.split('\n'):
        if line == "":
            continue

        name, expr = line.split(': ')
        orig_vals[name] = (False, expr)
        if expr.isdigit():
            orig_vals[name] = (True, int(expr))

    def rec(name, vals):
        if vals[name][0]:
            return vals[name][1]

        expr = vals[name][1]
        expr = expr.split(' ')
        assert len(expr) == 3
        a, op, b = expr
        v = eval(f"{rec(a, vals)} {op} {rec(b, vals)}")
        vals[name] = (True, v)
        return v

    x1, _, x2 = orig_vals["root"][1].split(' ')

    i_upper, i_lower = 10000000000000000000, 0

    while i_upper > i_lower:
        vals = orig_vals.copy()
        new = (i_upper - i_lower) // 2 + i_lower
        vals["humn"] = (True, new)
        y1 = rec(x1, vals)
        y2 = rec(x2, vals)

        if y1 < y2:
            i_upper = new
        if y1 > y2:
            i_lower = new

        if y1 == y2:
            return new


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
