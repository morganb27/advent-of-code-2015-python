from collections import defaultdict
import re

PUZZLE = [line.strip() for line in open("input.txt")]
SCORE = defaultdict(dict)
PART_1, PART_2 = 0, 0

for line in PUZZLE:
    ingredient, capacity, durability, flavor, texture, calories = re.search(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line).groups()
    SCORE[ingredient] = {
        "capacity": int(capacity),
        "durability": int(durability),
        "flavor": int(flavor),
        "texture": int(texture),
        "calories": int(calories)
    }

def teaspoon(total):
    for a in range(total + 1):
        for b in range(total - a + 1):
            for c in range(total - a - b + 1):
                d = total - a - b - c
                yield(a, b, c , d)

INGREDIENTS = list(SCORE.keys())

for combo in teaspoon(100):
    capacity = max(0, sum(SCORE[ing]["capacity"] * amt for ing, amt in zip(INGREDIENTS, combo)))
    durability = max(0, sum(SCORE[ing]["durability"] * amt for ing, amt in zip(INGREDIENTS, combo)))
    flavor = max(0, sum(SCORE[ing]["flavor"] * amt for ing, amt in zip(INGREDIENTS, combo)))
    texture = max(0, sum(SCORE[ing]["texture"] * amt for ing, amt in zip(INGREDIENTS, combo)))
    calories = sum(SCORE[ing]["calories"] * amt for ing, amt in zip(INGREDIENTS, combo))

    PART_1 = max(PART_1, capacity * durability * flavor * texture)

    if calories == 500:
        PART_2 = max(PART_2, capacity * durability * flavor * texture)


print("PART_1:", PART_1)
print("PART_2:", PART_2)

