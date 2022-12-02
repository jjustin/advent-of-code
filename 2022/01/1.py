from input import input

best = -1
for elf in input.split('\n\n'):
    elfSum = sum([int(x) for x in elf.split('\n')])
    best = max(elfSum, best)

print(best)
