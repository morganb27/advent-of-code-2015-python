from utils import Point, DIRS_8

PUZZLE = [line.strip() for line in open("input.txt")]

m = len(PUZZLE) #ord
n = len(PUZZLE[0]) #abs
CORNERS = {Point(0, 0), Point(n - 1, 0), Point(0, -(m - 1)), Point(n - 1, -(m - 1))}

def init_state():
    ON, OFF = set(), set()
    for y, _ in enumerate(PUZZLE):
        for x, _ in enumerate(PUZZLE[y]):
            if PUZZLE[y][x] == "#":
                ON.add(Point(x, -y))
            else:
                OFF.add(Point(x, -y))
    return ON, OFF

def step(ON, OFF, part_2 = False):
    new_on, new_off = set(), set()
    for light in ON:
        if part_2 and light in CORNERS:
            new_on.add(light)
            continue
        count = 0
        for dir in DIRS_8:
            if light + dir in ON:
                count += 1
        if count == 2 or count == 3:
            new_on.add(light)
        else:
            new_off.add(light)
    

    for light in OFF:
        if part_2 and light in CORNERS:
            new_off.add(light)
            continue
        count = 0
        for dir in DIRS_8:
            if light + dir in ON:
                count += 1
        if count == 3:
            new_on.add(light)
        else:
            new_off.add(light)
    
    return new_on, new_off


def run(steps, part_2 = False):
    ON, OFF = init_state()
    for _ in range(steps):
        ON, OFF = step(ON, OFF, part_2)
    return len(ON)



# Part 1
print("PART_1:", run(100, part_2=False))

# Part 2
print("PART_2:", run(100, part_2=True))