from utils import ints

PUZZLE = [line.strip() for line in open("input.txt")]
GRID = [[0 for _ in range(1000)] for _ in range(1000)]
GRID_TWO = [[0 for _ in range(1000)] for _ in range(1000)]

def get_instruction(s):
    if s.startswith("turn on"):
        return "on"
    elif s.startswith("turn off"):
        return "off"
    else:
        return "toggle"

for line in PUZZLE:
    instruction = get_instruction(line)
    x1, y1, x2, y2 = ints(line)

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):

            # Part 1
            if instruction == "on":
                GRID[i][j] = 1
            elif instruction == "off":
                GRID[i][j] = 0
            elif instruction == "toggle":
                GRID[i][j] ^= 1

            # Part 2
            if instruction == "on":
                GRID_TWO[i][j] += 1
            elif instruction == "off":
                GRID_TWO[i][j] = max(0, GRID_TWO[i][j] - 1)
            elif instruction == "toggle":
                GRID_TWO[i][j] += 2

PART_1 = sum(light for row in GRID for light in row if light == 1)
PART_2 = sum(light for row in GRID_TWO for light in row)

print(PART_1)
print(PART_2)