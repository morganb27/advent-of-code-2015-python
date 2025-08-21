from itertools import combinations
from collections import defaultdict

PUZZLE = [line.strip() for line in open("input.txt")]

CONTAINERS = []
TARGET = 150
PART_1 = 0
WAYS = defaultdict(int)

for line in PUZZLE:
    CONTAINERS.append(int(line))


for i in range(len(CONTAINERS)):
    for comb in combinations(CONTAINERS, i):
        if sum(comb) == TARGET:
            PART_1 += 1
            WAYS[len(comb)] += 1

PART_2 = WAYS[min(WAYS)]
print("PART_1", PART_1)
print("PART_2", PART_2)
