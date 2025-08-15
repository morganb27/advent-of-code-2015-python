import re
from collections import defaultdict
from itertools import permutations

PUZZLE = [line.strip() for line in open("input.txt")]
GRAPH = defaultdict(dict)
SUM = 0

def parse_line(line):
    p1, diff, score, p2 = re.search(r"(\w+) .* (gain|lose) (\d+) .* (\w+).", line).groups()
    return p1, int(score) * (-1 if diff == "lose" else 1), p2


for line in PUZZLE:
    p1, score, p2 = parse_line(line)
    GRAPH[p1][p2] = score

# Add myself for part 2
for p in list(GRAPH.keys()):
    GRAPH["Morgan"][p] = 0
    GRAPH[p]["Morgan"] = 0


for perm in permutations(GRAPH.keys()):
    count = 0
    for i in range(len(perm)):
        cur = perm[i]
        next = perm[(i + 1) % len(perm)]
        prev = perm[(i - 1) % len(perm)]
        count += GRAPH[cur][next]
        count += GRAPH[cur][prev]
    SUM = max(SUM, count)

print(SUM)
