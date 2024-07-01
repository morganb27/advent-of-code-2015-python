import fileinput
import ast
import re

PUZZLE = [line.strip() for line in fileinput.input()]
raw, literal, encoded_chars = 0, 0, 0

def matchsticks():
    for line in PUZZLE:
        raw += len(line)
        literal += len(ast.literal_eval(line))
    return -1

matchsticks()
print(f"Solution for part 1 is: {raw - literal}")
print(f"Solution for part 1 is {encoded_chars - raw}")

