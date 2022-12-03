from input import input

score = 0
LOSE, DRAW, WIN = 0, 3, 6
resultTable = {
    "A": {
        "X": DRAW,
        "Y": WIN,
        "Z": LOSE,
    },
    "B": {
        "X": LOSE,
        "Y": DRAW,
        "Z": WIN,
    },
    "C": {
        "X": WIN,
        "Y": LOSE,
        "Z": DRAW,
    },
}
scoring = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

for round in input.split("\n"):
    [opp, you] = round.split(" ")
    score += resultTable[opp][you] + scoring[you]

print(score)
