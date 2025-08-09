from collections import defaultdict
from itertools import permutations

PUZZLE = [line.strip() for line in open("input.txt")]
PART_1, PART_2 = float("inf"), 0
GRAPH = defaultdict(dict)
CITIES = set()

for line in PUZZLE:
    left, right = line.split(" = ")
    d1, d2 = left.split(" to ")
    distance = int(right)

    GRAPH[d1][d2] = distance
    GRAPH[d2][d1] = distance
    CITIES.add(d1)
    CITIES.add(d2)

for perm in permutations(CITIES):
    distance = 0
    for a, b in zip(perm, perm[1:]):
        distance += GRAPH[a][b]
    PART_1 = min(PART_1, distance)
    PART_2 = max(PART_2, distance)


print(GRAPH)
print(PART_1)
print(PART_2)