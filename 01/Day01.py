import fileinput

PUZZLE = [line.strip() for line in fileinput.input()][0]

def solve_part_1(data):
    count = 0
    for char in data:
        if char == '(':
            count+=1
        elif char == ')':
            count-=1
    return count

print(f"Solution to part 1 is: {solve_part_1(PUZZLE)}")

def solve_part_2(data):
    count = 0
    for i in range(len(data)):
        count += 1 if data[i] == '(' else -1
        if count == -1:
            return "Santa just entered floor -1 at index: ", i + 1
    return count


print(f"Solution to part 2: {solve_part_2(PUZZLE)}")