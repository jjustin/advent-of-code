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
    input = [(int(x)*811589153, i) for i, x in enumerate(input.split('\n'))]

    for _ in range(10):
        for i in range(len(input)):
            v, p, original_pos = [(val, pos, original_pos) for pos, (val, original_pos)
                                  in enumerate(input) if original_pos == i][0]
            t = (v, original_pos)
            newp = (p + v) % (len(input)-1)

            del input[p]
            input.insert(newp, t)

    input = [x for x, _ in input]
    zero_ix = input.index(0)

    s = sum(input[(zero_ix + d) % len(input)] for d in [1000, 2000, 3000])
    return s


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

sample_input = """1
2
-3
3
-2
0
4"""
sample_res = 1623178306

sample_out = solve(sample_input)
print(sample_out)
if sample_out != sample_res:
    print("Sample incorrect!!")
    exit()


out = solve(input)
handle_result(str(out))
