import os
import subprocess
import itertools as it


def handle_result(result):
    subprocess.run("pbcopy", text=True, input=result)
    print(result)


def solve(input: str):
    dir_path = ""
    dirs = []
    files = {}

    for command in input.split('$ ')[1:]:
        [cmd, output] = command.split("\n", 1)

        if cmd == "ls":
            for out_line in output.split("\n"):
                if out_line == "":
                    continue
                if out_line.startswith("dir"):
                    dirs.append(dir_path+"/"+out_line[4:])
                else:
                    [size, name] = out_line.split(" ")
                    size = int(size)
                    files[dir_path+"/"+name] = size
        if cmd.startswith("cd"):
            assert output == ""
            dir = cmd[3:]
            if dir == "..":
                dir_path = "/".join(dir_path.split("/")[:-1])
            elif dir == "/":
                dir_path = ""
            else:
                dir_path = dir_path + "/" + dir

    required_space = 30000000
    disk_size = 70000000
    used_size = sum(files.values())
    min_dir_size = required_space - (disk_size - used_size)

    sums = []
    for dir in dirs:
        sum_dir = 0
        for path, size in files.items():
            if path.startswith(dir+"/"):
                sum_dir += size
        if sum_dir >= min_dir_size:
            sums.append(sum_dir)
    return min(sums)


with open(f"{os.path.dirname(__file__)}/input", "r") as f:
    input = f.read()

out = solve(input)
handle_result(str(out))
