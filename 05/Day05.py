import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
FORBIDDEN = ["ab", "cd", "pq", "xy"]
VOWELS = "aeiou"

def nice_strings_part_one(data):
    count = 0
    for line in data:
        if isNiceString(line):
            count += 1
    return count

def nice_strings_part_two(data):
    count = 0
    for line in data:
        if isNiceStringPart2(line):
            count += 1
    return count



def isNiceString(s):
    countVowel = 0
    pairs = False
    for i, c in enumerate(s):
        if c in VOWELS:
            countVowel+=1
        if i < len(s) - 1:
            contiguous = s[i] + s[i+1]
            if contiguous in FORBIDDEN:
                return False
            if s[i] == s[i+1]:
                pairs = True
    return countVowel >= 3 and pairs

def isNiceStringPart2(s):
    repeat = False
    pairs = {}
    hasTwoPairs = False
    for i, c in enumerate(s):
        if i < len(s) - 2:
            if s[i] == s[i+2]:
                print(s[i], s[i+2])
                repeat = True
        if i < len(s) - 1:
            contiguous = s[i:i+2]
            if contiguous in pairs and i - pairs[contiguous] > 1:
                hasTwoPairs = True
                print("hastwopairs")
            else:
                pairs[contiguous] = i
    print(pairs)
    return hasTwoPairs and repeat
    

print(f"The number of nice strings is: {nice_strings_part_one(PUZZLE)}")
print(f"The number of nice strings for part 2 is {nice_strings_part_two(PUZZLE)}")