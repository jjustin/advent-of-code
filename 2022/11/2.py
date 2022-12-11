import itertools as it
import os
import subprocess
import functools
import numpy as np
try:
    from utils import *
except ImportError:
    print("No utils found, not importing.")


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


def solve(input: str):
    input = input.split('\n\n')
    monkeys = [None] * len(input)
    lcm = 1

    for monkey in input:
        if monkey == "":
            continue
        lines = monkey.split('\n')

        monkey_name = int(lines[0].split(':')[0].split(" ")[1].strip())

        items = lines[1].split(':')[1].strip().split(',')
        items = [int(i) for i in items]

        operation = lines[2].split(':')[1].strip()
        operation = operation.split(' ')

        test = int(lines[3].split(':')[1].strip().split(' ')[2])
        lcm *= test

        if_true = int(lines[4].split(':')[1].split(' ')[4])
        if_false = int(lines[5].split(':')[1].split(' ')[4])

        monkeys[monkey_name] = {
            'items': items,
            'operation': operation,
            'test': test,
            'if_true': if_true,
            'if_false': if_false
        }

    activness = [0] * len(monkeys)
    for round in range(10000):
        for monkey_id, monkey in enumerate(monkeys):
            operation = monkey['operation']
            test = monkey['test']
            if_true = monkey['if_true']
            if_false = monkey['if_false']
            items = monkey['items']

            for item in items:
                activness[monkey_id] += 1

                old = item
                new = eval(" ".join(operation[2:]))
                new = new % lcm

                pass_to = int(if_false)
                if new % test == 0:
                    pass_to = int(if_true)

                monkeys[pass_to]["items"].append(new)
            monkeys[monkey_id]["items"] = []

    activness.sort()
    return activness[-1] * activness[-2]


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(str(out))
