from utils import Point

PUZZLE = open("input.txt").read()

DIR = {
    "^": Point(0, 1),
    "v": Point(0, -1),
    ">": Point(1, 0),
    "<": Point(-1, 0),
}

# Part 1
POS = Point(0, 0)
VISITED = {POS}

for move in PUZZLE:
    POS += DIR[move]
    VISITED.add(POS)

PART_1 = len(VISITED)

# Part 2
SANTA = Point(0, 0)
ROBOT = Point(0, 0)
VISITED_TWO = {Point(0, 0)}

for i, move in enumerate(PUZZLE):
    if i % 2 == 0:
        SANTA += DIR[move]
        VISITED_TWO.add(SANTA)
    else:
        ROBOT += DIR[move]
        VISITED_TWO.add(ROBOT)

PART_2 = len(VISITED_TWO)

print(PART_1)
print(PART_2)
