import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
import parse
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    res = "no result provided"
    res = 0
    input = input.strip()
    input = input.split('\n\n')
    for i, pair in enumerate(input):
        [p1, p2] = pair.split('\n')
        p1 = eval(p1)
        p2 = eval(p2)
        print(p1, p2)
        if compare(p1, p2)[0]:
            print("in order")
            res += i+1

    return res


def compare(p1, p2):
    if p1 == p2:
        return True, True
    if isinstance(p1, int) and isinstance(p2, int):
        return p1 < p2, False
    if isinstance(p1, int) and isinstance(p2, list):
        p1 = [p1]
        return compare(p1, p2)
    if isinstance(p1, list) and isinstance(p2, int):
        p2 = [p2]
        return compare(p1, p2)

    for i in range(max(len(p1), len(p2))):
        if i >= len(p1):
            return True, False
        if i >= len(p2):
            return False, False
        t, cont = compare(p1[i], p2[i])
        if not cont:
            return t, False
        if not t:
            return False

    return True, True


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


out = solve(input)
handle_result(str(out))
