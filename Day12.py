import json

PUZZLE = json.load(open("input.txt"))


def sum_numbers(data, skip_red = False):
    if isinstance(data, list):
        return sum(sum_numbers(x, skip_red) for x in data)
    elif isinstance(data, dict):
        if skip_red and "red" in data.values():
            return 0
        return sum(sum_numbers(value, skip_red) for _, value in data.items())
    elif isinstance(data, int):
        return data
    else:
        return 0



PART_1 = sum_numbers(PUZZLE)
PART_2 = sum_numbers(PUZZLE, skip_red=True)
print(PART_1)
print(PART_2)