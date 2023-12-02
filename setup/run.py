#!/usr/bin/env python
import argparse
import os
import subprocess

from parse import parseargs

if __name__ == "__main__":
    day, year = parseargs()

    root_dir = os.path.dirname(__file__)
    file_dir = f"{root_dir}/../{year}/{day:02d}/"

    challenge = 1
    if os.path.isfile(file_dir + "2.py"):
        challenge = 2

    filename = file_dir + f"{challenge}.py"

    print(f"running {challenge}")
    subprocess.run(["python", filename])
