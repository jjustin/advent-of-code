#!/usr/bin/env python
import functools as ft
import itertools as it
import os
import re
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

    r = r"mul\(\d{1,3},\d{1,3}\)"

    for match in re.finditer(r, input):
        mul = lambda x, y: x * y
        res += eval(match.group())

    return res


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
