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
    for line in input.split("\n"):
        if line == "":
            continue
        first = None
        last = None
        l = ""
        for line_start in range(len(line)):
            for line_end in range(line_start, min(len(line) + 1, line_start + 6)):
                substr = line[line_start:line_end]

                if substr == "one":
                    l += "1"
                if substr == "two":
                    l += "2"
                if substr == "three":
                    l += "3"
                if substr == "four":
                    l += "4"
                if substr == "five":
                    l += "5"
                if substr == "six":
                    l += "6"
                if substr == "seven":
                    l += "7"
                if substr == "eight":
                    l += "8"
                if substr == "nine":
                    l += "9"
                if substr == "zero":
                    l += "0"
                if substr in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                    l += substr

        for char in l:
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                if first is None:
                    first = int(char)
                last = int(char)

        if first is not None and last is not None:
            res += 10 * first + last

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
