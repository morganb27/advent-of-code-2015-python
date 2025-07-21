import os
import sys
import requests

day = int(sys.argv[1])
session = os.getenv("AOC_SESSION")
if not session:
    raise RuntimeError("Missing AOC_SESSION environment variable.")

url = f"https://adventofcode.com/2015/day/{day}/input"
response = requests.get(url, cookies={"session": session})

if response.status_code != 200:
    raise RuntimeError(f"Failed to fetch input (status {response.status_code})")


with open("input.txt", "w") as f:
    f.write(response.text.strip())

print(f"input.txt written for day {day}")
