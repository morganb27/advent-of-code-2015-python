import ast
import json

PUZZLE = [line.strip() for line in open("input.txt")]
PART_1, PART_2 = 0, 0

for line in PUZZLE:
    chars = len(ast.literal_eval(line))
    encoded = json.dumps(line)

    PART_1 += len(line) - chars
    PART_2 += (len(encoded) - len(line))
print(PART_1)
print(PART_2)