from input import input


def score(intersect):
    if ord(intersect) > ord('Z'):
        return ord(intersect) - ord('a') + 1
    else:
        return ord(intersect) - ord('A') + 27


sum = 0

for items in input.split('\n'):
    p1 = items[:len(items)//2]
    p2 = items[len(items)//2:]
    intersect = ""
    for i in p1:
        if i in p2 and not i in intersect:
            intersect += i
    sum += score(intersect)

print(sum)
