import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
from parse import *
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def solve(input: str):
    input = input.strip()
    res = "no result provided"
    g = {}
    for line in input.split('\n'):
        if line == "":
            continue

        x = parse("Valve {} has flow rate={}; tunnels lead to valves {}", line)
        if x == None:
            x = parse("Valve {} has flow rate={}; tunnel leads to valve {}", line)

        valve, rate, tunnels = x
        rate = int(rate)
        g[valve] = {
            "rate": int(rate),
            "tunnels": tunnels.split(", ")
        }

    dists = calc_dists(g)
    # print(dists)
    s = simulate(g, "AA", [], 0, 0, dists)
    print(s)
    return s[0]


def simulate(g, pos, open, score, time, dists):
    unopened = list(filter(lambda x: x not in open, g))
    possible = []

    for valve in unopened:
        if g[valve]["rate"] == 0:
            continue

        time_needed = dists[pos][valve] + 1

        if time + time_needed >= 30:
            score_new = inc_score(g, open, score, 30 - time)
            possible.append([score_new, []])
            continue

        score_new = inc_score(g, open, score, time_needed)
        score_new = simulate(
            g, valve, open + [valve], score_new, time + time_needed, dists)

        possible.append(
            [score_new[0], [valve, time+time_needed] + score_new[1]])

    if len(possible) == 0:
        return (inc_score(g, open, score, 30-time), [])

    return max(possible, key=lambda x: x[0])


def inc_score(g, open, score, duration):
    for valve in open:
        score += duration * g[valve]["rate"]
    return score


def calc_dists(g):
    dists = {}
    """calculate shortest from each valve to each valve"""
    for valve in g:
        dists[valve] = {}
        for other in g:
            dists[valve][other] = calc_dist(g, valve, other)
    return dists


def calc_dist(g, valve, other):
    if valve == other:
        return 0

    dist = 0
    visited = set()
    queue = g[valve]["tunnels"]
    while len(queue) > 0:
        dist += 1
        new_queue = []
        for v in queue:
            if v == other:
                return dist
            visited.add(v)
            for tunnel in g[v]["tunnels"]:
                if tunnel not in visited:
                    new_queue.append(tunnel)
        queue = new_queue

    return None


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
