PUZZLE = [line.strip() for line in open("input.txt")]

forbidden = ["ab", "cd", "pq", "xy"]
PART_1 = 0
PART_2 = 0

# Part 1
for line in PUZZLE:
    vowel_count = sum(c in "aeiou" for c in line)
    has_double = any(a == b for a, b in zip(line, line[1:]))
    has_forbidden = any(pair in line for pair in forbidden)

    if vowel_count >= 3 and has_double and not has_forbidden:
        PART_1 += 1

# Part 2
for line in PUZZLE:
    has_letter_repeat = any(line[i] == line[i+2] for i in range(len(line) - 2))

    has_pair = False
    pairs = {}

    for i in range(len(line) - 1):
        pair = line[i:i+2]

        if pair in pairs and pairs[pair] + 1 < i:
            has_pair = True
            break
        elif pair not in pairs:
            pairs[pair] = i 
    
    if has_letter_repeat and has_pair:
        p2 += 1


print(PART_1)
print(PART_2)