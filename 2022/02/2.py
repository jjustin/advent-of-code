from input import input

score = 0

lose = {
    'A': 3,
    "B": 1,
    "C": 2
}
win = {
    'A': 2,
    "B": 3,
    "C": 1
}
draw = {
    'A': 1,
    "B": 2,
    "C": 3
}
scoring = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

for round in input.split("\n"):
    [opp, outcome] = round.split(" ")
    score += scoring[outcome]
    if outcome == "X":
        score += lose[opp]
    if outcome == "Y":
        score += draw[opp]
    if outcome == "Z":
        score += win[opp]


print(score)
