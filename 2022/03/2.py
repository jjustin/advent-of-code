from input import input


def score(intersect):
    if ord(intersect) > ord('Z'):
        return ord(intersect) - ord('a') + 1
    else:
        return ord(intersect) - ord('A') + 27


sum = 0
x = input.split('\n')
for i in range(0, len(x), 3):
    [p1, p2, p3] = x[i:i+3]
    intersect = ""
    for i in p1:
        if i in p2 and i in p3 and not i in intersect:
            intersect += i
    sum += score(intersect)

print(sum)
