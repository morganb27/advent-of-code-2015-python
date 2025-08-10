from itertools import groupby

PUZZLE = "3113322113"

def process(s):
    sequence = ""
    for key, group in groupby(s):
        sequence += str(len(list(group))) + key
    return sequence

for _ in range(50):
    PUZZLE = process(PUZZLE)

print(len(PUZZLE))

