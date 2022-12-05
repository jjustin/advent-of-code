from input import input


c = 0
for pair in input.split("\n"):
    [x, y] = pair.split(",")
    [x1, x2] = x.split("-")
    x1 = int(x1)
    x2 = int(x2)
    [y1, y2] = y.split("-")
    y1 = int(y1)
    y2 = int(y2)

    if x1 <= y1 and x2 >= y2:
        c += 1
    elif y1 <= x1 and y2 >= x2:
        c += 1

print(c)
