import fileinput
from collections import defaultdict
from itertools import permutations

PUZZLE = [line.strip() for line in fileinput.input()]

def shortest_distance(data):
    graph = defaultdict(dict)
    shortest = float("inf")
    longest = float("-inf")
    for line in data:
        x, y, dist = parse_input(line)
        graph[x][y] = int(dist)
        graph[y][x] = int(dist)
    for perm in permutations(graph.keys()):
        sum = 0
        for i in range(len(perm) - 1):
            sum += graph[perm[i]][perm[i+1]]
        shortest = min(shortest, sum)
        longest = max(longest, sum)
    return shortest, longest
        


def parse_input(line):
    left, dist = [x.strip() for x in line.split(" = ")]
    x, y = [c.strip() for c in left.split(" to ")]
    return x, y, dist

print(f"The distance of the shortest and the longest routes are: {shortest_distance(PUZZLE)}")