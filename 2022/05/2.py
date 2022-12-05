from input import input

stacks = {}
init_phase = True

for line in input.split('\n'):
    if init_phase:
        if line == "":
            print(stacks)
            init_phase = False
            continue
        crates = [line[i+1:i+2] for i in range(0, len(line), 4)]
        for (i, crate) in enumerate(crates, 1):
            if crate == " ":
                continue
            if i not in stacks:
                stacks[i] = ""
            stacks[i] += crate
        continue

    [_, num, _, fr, _, to] = line.split(" ")
    num, fr, to = int(num), int(fr), int(to)

    move = stacks[fr][:num]
    stacks[fr] = stacks[fr][num:]
    stacks[to] = move + stacks[to]

x = ""
for i in range(1, len(stacks)+1):
    x += stacks[i][0]
print(x)
