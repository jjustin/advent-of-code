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
    res = 0

    for line in input.split('\n'):
        if line == "":
            continue

        res += snafuToDec(line)

    return decToSnafu(res)


SNAFU_DEC_MAPPING = {
    "0": 0,
    "1": 1,
    "2": 2,
    "=": -2,
    "-": -1,
}


def snafuToDec(n):
    return 5 * snafuToDec(n[:-1]) + SNAFU_DEC_MAPPING[n[-1]] if n else 0


def decToSnafu(n):
    if n > 0:
        return decToSnafu((n+2)//5) + "012=-"[n % 5]
    return ""


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
