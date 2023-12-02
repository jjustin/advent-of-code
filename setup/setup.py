#!/usr/bin/env python
import os
import shutil
import subprocess
import time
import webbrowser

from parse import err, parseargs

if __name__ == "__main__":
    day, year = parseargs()

    root_dir = os.path.dirname(__file__)

    destination_dir = f"{root_dir}/../{year}/{day:02d}/"
    input_file = destination_dir + "input"
    destination_file = destination_dir + "1.py"

    if os.path.isfile(destination_file):
        err(f"File {destination_file} already exists")

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    shutil.copy(f"{root_dir}/template.py", destination_file)

    f = open(input_file, "w")
    f.close()

    subprocess.run(["code", destination_file], check=True)
    subprocess.run(["code", input_file], check=True)
    time.sleep(0.2)
    webbrowser.open(f"https://adventofcode.com/{year}/day/{day}")

    print(f"Getting day {day} from year {year}")
