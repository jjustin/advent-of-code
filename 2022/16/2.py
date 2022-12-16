import itertools as it
import os
import subprocess
import functools as ft
import numpy as np
from parse import *
from collections import defaultdict
from frozendict import frozendict
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


import re

r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

V, F, D = set(), dict(), defaultdict(lambda: 1000)

for v, f, us in re.findall(r, open('16/input').read()):
    V.add(v)                                  # store node
    if f != '0':
        F[v] = int(f)                # store flow
    for u in us.split(', '):
        D[u, v] = 1       # store dist

for k, i, j in it.product(V, V, V):    # floyd-warshall
    D[i, j] = min(D[i, j], D[i, k] + D[k, j])


def solve(input: str):
    input = input.strip()
    res = "no result provided"
    valves, flows, tunnels = set(), {}, defaultdict(lambda: 9999999)
    for line in input.split('\n'):
        if line == "":
            continue

        x = parse("Valve {} has flow rate={}; tunnels lead to valves {}", line)
        if x == None:
            x = parse("Valve {} has flow rate={}; tunnel leads to valve {}", line)

        valve, rate, tunnels2 = x
        tunnels2 = tunnels2.split(', ')
        rate = int(rate)

        valves.add(valve)

        if rate != 0:
            flows[valve] = rate

        for tunnel in tunnels2:
            tunnels[valve, tunnel] = 1

    # calculate shortest paths
    for k, i, j in it.product(valves, valves, valves):
        tunnels[i, j] = min(tunnels[i, j], tunnels[i, k] + tunnels[k, j])

    s = simulate("AA", 26, frozenset(flows.keys()),
                 frozendict(flows), frozendict(tunnels))
    return s


@ft.cache
def simulate(curr, time_left, valves, flows, tunnels, el_avail=True):
    possible = []
    # iterate over all valves for current actor and calculate score increase for each
    for v in valves:
        if tunnels[curr, v] < time_left:
            # Time remaining after traveling to valve v and opening it
            t = time_left-tunnels[curr, v]-1
            # Total score received by opening valve v
            score = (flows[v] * t)
            # get best solution for remaining valves starting from valve v
            score += simulate(v, t, valves - {v}, flows, tunnels, el_avail)

            possible.append(score)

    score = 0
    if el_avail:
        # Check how many valves we can open using the elephant in 26 minutes on top of the valves we have already opened
        score = simulate("AA", 26, valves, flows, tunnels, False)

    return max(possible + [score])


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()


out = solve(input)
handle_result(str(out))
