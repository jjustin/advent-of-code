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

    return rec("root", orig_vals)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
