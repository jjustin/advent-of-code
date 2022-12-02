from input import input

best = -1
elfs = [sum([int(x) for x in elf.split('\n')]) for elf in input.split('\n\n')]

elfs.sort()

print(sum(elfs[-3:]))
