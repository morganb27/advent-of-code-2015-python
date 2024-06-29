import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]



def decorate_house(data):
    rows, cols = (1000, 1000)
    lights = [[0 for i in range(rows)] for j in range(cols)]
    for line in data:
        instruction, rowStart, rowEnd, columnStart, columnEnd = parse_input(line)
        for i in range(rowStart, rowEnd + 1):
            for j in range(columnStart, columnEnd + 1):
                if instruction == "toggle":
                    lights[i][j] ^= 1
                elif instruction == "on":
                    lights[i][j] = 1
                elif instruction == "off":
                    lights[i][j] = 0
    return sum(sum(x) for x in lights)

def decorate_house_part_2(data):
    rows, cols = (1000, 1000)
    lights = [[0 for i in range(rows)] for j in range(cols)]
    for line in data:
        instruction, rowStart, rowEnd, columnStart, columnEnd = parse_input(line)
        for i in range(rowStart, rowEnd + 1):
            for j in range(columnStart, columnEnd + 1):
                if instruction == "toggle":
                    lights[i][j] += 2
                elif instruction == "on":
                    lights[i][j] += 1
                elif instruction == "off":
                    lights[i][j] -= 1 if lights[i][j] > 0 else 0
    return sum(sum(x) for x in lights)
    

def parse_input(line):
    lst = line.split(' ')
    if lst[0] == "toggle":
        instruction = "toggle"
        rowStart, columnStart = [int(x.strip()) for x in lst[1].split(',')]
        rowEnd, columnEnd = [int(x.strip()) for x in lst[-1].split(',')]
    else:
        instruction = lst[1]
        rowStart, columnStart = [int(x.strip()) for x in lst[2].split(',')]
        rowEnd, columnEnd = [int(x.strip()) for x in lst[-1].split(',')]
    return instruction, rowStart, rowEnd, columnStart, columnEnd


print(f"Solution for part 1 is: {decorate_house(PUZZLE)}")
print(f"Solution for part 2 is: {decorate_house_part_2(PUZZLE)}")