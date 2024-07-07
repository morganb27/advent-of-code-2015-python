import fileinput
from collections import defaultdict
from itertools import permutations

PUZZLE = [line.strip() for line in fileinput.input()]

def happiness(data):
    result = 0
    graph = defaultdict(dict)
    for line in data:
        x, y, value = parse_input(line)
        graph[x][y] = value
    for perm in permutations(graph.keys()):
        count = 0
        for i in range(len(perm)):
            count += graph[perm[i]][perm[(i + 1) % len(perm)]]
            count += graph[perm[(i + 1) % len(perm)]][perm[i]]
        result = max(result, count)
    return result

def happiness_with_me(data):
    result = 0
    graph = defaultdict(dict)
    for line in data:
        x, y, value = parse_input(line)
        graph[x][y] = value
    for x in list(graph.keys()):
        graph[x]['Morgan'] = 0
        graph['Morgan'][x] = 0
    for perm in permutations(graph.keys()):
        count = 0
        for i in range(len(perm)):
            count += graph[perm[i]][perm[(i + 1) % len(perm)]]
            count += graph[perm[(i + 1) % len(perm)]][perm[i]]
        result = max(result, count)
    return result


def parse_input(line):
    arr = line.split(" ")
    x, y = arr[0], arr[-1].strip(".")
    value = int(arr[3]) if arr[2] == "gain" else int(arr[3]) * - 1
    return x, y, value


print(f"Total happiness for part 1 is: {happiness(PUZZLE)}")
print(f"Total happiness for part 2 is : {happiness_with_me(PUZZLE)}")