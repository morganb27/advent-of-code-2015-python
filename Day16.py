import re

PUZZLE = [line.strip() for line in open("input.txt")]

AUNT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

for i, line in enumerate(PUZZLE, start=1):
        key_one, value_one, key_two, value_two, key_three, value_three = re.search(r".*: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line).groups()
        aunt = {
            key_one: int(value_one),
            key_two: int(value_two),
            key_three: int(value_three)
        }

        if all(AUNT[key] == aunt[key] for key in aunt.keys()):
                PART_1 = i
        
        if all(
                AUNT[key] < aunt[key] if key in ["cats", "trees"]
                    else AUNT[key] > aunt[key] if key in ["pomeranians", "goldfish"] 
                    else AUNT[key] == aunt[key]  
                    for key in aunt.keys()
                ):
                PART_2 = i
print("PART_1", PART_1)
print("PART_2", PART_2)
