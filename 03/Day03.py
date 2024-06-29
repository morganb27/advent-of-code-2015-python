import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()][0]

directions = {
    '^': [0, 1],
    '>': [1, 0],
    'v': [0, -1],
    '<': [-1, 0]
}


def deliver_twice(data):
    count = 0
    santa = [0, 0]
    visited = defaultdict(int, {'0,0' : 1})
    for char in data:
        x, y = directions[char]
        santa[0] += x
        santa[1] += y
        visited[f"{santa[0]},{santa[1]}"] += 1
    
    for value in visited.values():
        if value >= 1:
            count+=1
    return count

def robot_santa(data):
    santa = [0, 0]
    robot = [0, 0]
    visited = set() 
    for i in range(len(data)):
        x, y = directions[data[i]]
        if i % 2 == 0:
            santa[0] += x
            santa[1] += y
            visited.add(f"{santa[0], santa[1]}")
        elif i % 2 != 0:
            robot[0] += x
            robot[1] += y
            visited.add(f"{robot[0], robot[1]}")
    return len(visited)
        


print(f"The number of houses which was visited at least once is {deliver_twice(PUZZLE)}")
print(f"Number of houses visited with robot is: {robot_santa(PUZZLE)}")