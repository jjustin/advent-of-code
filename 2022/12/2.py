import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
import parse
import queue
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):

    res = "no result provided"
    field = []
    input = input.strip()
    q = []
    for i, line in enumerate(input.split('\n')):
        if line == "":
            continue
        l = []
        for j, char in enumerate(line):
            o = ord(char)
            if char == 'S':
                o = ord('a')
            if char == 'E':
                e_x, e_y = i, j
                o = ord('z')
            if ord('a') == o:
                q.append((i, j, 0))
            l.append((o, False))
        field.append(l)

    depth = 0
    while len(q) > 0:
        q_new = []
        for x, y, depth in q:
            if x == e_x and y == e_y:
                return depth
            if field[x][y][1]:
                continue
            field[x][y] = (field[x][y][0], True)

            if x+1 < len(field) and field[x+1][y][0] <= field[x][y][0]+1:
                q_new.append((x+1, y, depth+1))
            if x-1 >= 0 and field[x-1][y][0] <= field[x][y][0]+1:
                q_new.append((x-1, y, depth+1))
            if y+1 < len(field[0]) and field[x][y+1][0] <= field[x][y][0]+1:
                q_new.append((x, y+1, depth+1))
            if y-1 >= 0 and y-1 and field[x][y-1][0] <= field[x][y][0]+1:
                q_new.append((x, y-1, depth+1))

        # filter duplicates
        q = list(dict.fromkeys(q_new))
        # filter visited
        q = list(filter(lambda x: not field[x[0]][x[1]][1], q))
    return res


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


out = solve(input)
handle_result(str(out))
