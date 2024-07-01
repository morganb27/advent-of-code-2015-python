import fileinput
from collections import defaultdict, deque

PUZZLE = [line.strip() for line in fileinput.input()]


def wires(data):
    d = defaultdict(int)
    q = deque(data)
    while q:
        line = q.popleft()
        print(len(q))
        s1, s2, inst, value, dest = parse_input(line)
        if value is not None:
            d[dest] = value
        elif inst == "AND" and s1 in d and s2 in d:
            if s1.isdigit():
                d[dest] = int(s1) & d[s2]
            else:
                d[dest] = d[s1] & d[s2]
        elif inst == "OR" and s1 in d and s2 in d:
            d[dest] = d[s1] | d[s2]
        elif inst == "LSHIFT" and s1 in d:
            d[dest] = d[s1] << int(s2)
        elif inst == "RSHIFT" and s1 in d:
            d[dest] = d[s1] >> int(s2)
        elif inst == "NOT" and s1 in d:
            d[dest] = ~d[s1] & 0xFFFF
        else:
            q.append(line)
        if 'a' in d:
            return d
        print(q[0])
    return -1

    

def parse_input(line):
    s1, s2, inst, value, dest = "", "", "", None, ""
    left, dest = [x.strip() for x in line.split(' -> ')]
    if left.isdigit():
        value = int(left)
    elif any(op in left for op in ["AND", "OR", "LSHIFT", "RSHIFT"]):
        arr = left.split(" ")
        s1, s2, inst = arr[0], arr[2], arr[1]
    elif "NOT" in left:
        arr = left.split(" ")
        inst, s1 = arr[0], arr[1]
    return s1, s2, inst, value, dest


print(f"Value of the last signal to wire a is: {wires(PUZZLE)}")