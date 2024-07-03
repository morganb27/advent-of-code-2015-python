PUZZLE = "3113322113"

def look_and_say(s):
    number = s[0]
    occurence = 0
    sequence = ''
    
    for n in s:
        if number == n:
            occurence+=1
        else:
            sequence += str(occurence) + number
            number = n
            occurence = 1
    sequence += str(occurence) + number
    return sequence

for _ in range(40):
    PUZZLE = look_and_say(PUZZLE)

print(f"Solution for part 1 is: {len(PUZZLE)}")

for _ in range(10):
    PUZZLE = look_and_say(PUZZLE)

print(f"Solution for part 2 is: {len(PUZZLE)}")

