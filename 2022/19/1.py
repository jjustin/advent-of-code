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

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


def solve(input: str):
    input = input.strip()
    res = []

    for line in input.split('\n'):
        if line == "":
            continue
        bp = {i: {} for i in range(4)}

        id, bp[ORE][ORE], bp[CLAY][ORE], bp[OBSIDIAN][ORE], bp[OBSIDIAN][CLAY], bp[GEODE][ORE], bp[GEODE][OBSIDIAN] = parse(
            "Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.", line)
        print("Blueprint", id)
        robots = [1, 0, 0, 0]
        resources = [0, 0, 0, 0]

        q = {(tuple(robots), tuple(resources))}
        seen = set()
        for minute in range(24):
            max_geodes = 0
            new_q = set()
            for x in q:
                if x in seen:
                    continue

                robots, resources = x

                new_resources = [resources[i] + robots[i] for i in range(4)]
                max_geodes = max(max_geodes, new_resources[GEODE])

                # no reason in hoarding ore - build nothing only if there is not enough ore
                if resources[ORE] <= 6:
                    new_q.add((tuple(robots), tuple(new_resources)))

                for robot in range(4):
                    if all(bp[robot][i] <= resources[i] for i in bp[robot]):
                        new_robots = [robots[i] +
                                      (1 if i == robot else 0) for i in range(4)]
                        nresources = [new_resources[i] - (bp[robot][i] if i in bp[robot] else 0)
                                      for i in range(4)]
                        new_q.add((tuple(new_robots), tuple(nresources)))
            seen.update(q)
            q = set()

            for x in new_q:
                if x[1][GEODE] + (23-minute) >= max_geodes:
                    q.add(x)

        res.append(id * max_geodes)
    return sum(res)


def score(robots, resources, time):
    return resources[GEODE] + (23-time) + (24-time) * robots[GEODE]


def get_permutations():
    for l in range(5):
        for subset in it.combinations(range(4), l):
            yield list(subset)


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
