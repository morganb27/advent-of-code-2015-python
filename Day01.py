PUZZLE = open("input.txt").read()


count = 0

PART_1 = sum(1 if p == "(" else -1 for p in PUZZLE)

for i, p in enumerate(PUZZLE, 1):
    if p == "(":
        count += 1
    else:
        count -= 1
    if count == -1:
        PART_2 = i
        break

print(PART_1)
print(PART_2)