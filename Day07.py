from collections import defaultdict, deque

PUZZLE = [line.strip() for line in open("input.txt")]

WIRES = defaultdict(int)
QUEUE = deque(PUZZLE)

while QUEUE:
    wire = QUEUE.popleft()
    left, right = wire.split(" -> ")
    left_split = left.strip().split()

    if any(not x.isdigit() and x not in WIRES and x.lower() == x for x in left_split):
        QUEUE.append(wire)
        continue

    elif len(left_split) == 1:
        WIRES[right] = int(left_split[0]) if left_split[0].isdigit() else WIRES[left_split[0]]
    
    elif len(left_split) == 2:
        WIRES[right] = ~WIRES[left_split[1]] & 0xFFFF
    
    elif len(left_split) == 3 and left_split[1] == "AND":
        a = int(left_split[0]) if left_split[0].isdigit() else WIRES[left_split[0]]
        b = int(left_split[2]) if left_split[2].isdigit() else WIRES[left_split[2]]

        WIRES[right] = a & b
    
    elif len(left_split) == 3 and left_split[1] == "OR":
        WIRES[right] = WIRES[left_split[0]] | WIRES[left_split[2]]
    
    elif len(left_split) == 3 and left_split[1] == "LSHIFT":
        WIRES[right] = WIRES[left_split[0]] << int(left_split[2])
    
    elif len(left_split) == 3 and left_split[1] == "RSHIFT":
        WIRES[right] = WIRES[left_split[0]] >> int(left_split[2])

print(WIRES["a"])

