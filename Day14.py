import re
from collections import defaultdict

PUZZLE = [line.strip() for line in open("input.txt")]
PART_1 = 0
TOTAL_TIME = 2503
RACE = defaultdict(int)
REINDEERS = defaultdict(tuple)
LEADERBOARD = defaultdict(int)

def parse_line(line):
    reindeer, speed, duration, rest = re.search(r"(\w+) .* (\d+) .* (\d+) .* (\d+).", line).groups()
    return reindeer, int(speed), int(duration), int(rest)

def fly(speed, duration, rest):
    cycle = duration + rest
    km = 0
    for i in range(TOTAL_TIME):
        if i % cycle < duration:
            km += speed
    return km

def fly_part_two(i, km, speed, duration, rest):
    cycle = duration + rest
    if i % cycle < duration:
        km += speed
    return km

for line in PUZZLE:
    reindeer, speed, duration, rest = parse_line(line)
    km = fly(speed, duration, rest)
    PART_1 = max(PART_1, km)

    #Needed for part 2
    REINDEERS[reindeer] = (speed, duration, rest)

for i in range(TOTAL_TIME):
    for key, value in REINDEERS.items():
        km = RACE[key]
        RACE[key] = fly_part_two(i, km, value[0], value[1], value[2])
    max_position = max(RACE.values())
    for key, value in RACE.items():
        if value == max_position:
            LEADERBOARD[key] += 1

PART_2 = max(LEADERBOARD.values())
    
print("PART_1", PART_1)
print("PART_2", PART_2)
