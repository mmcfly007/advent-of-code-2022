# Day 1: Calorie Counting

import sys

calories = 0
elves = []

for line in sys.stdin:
    line = line.strip()
    if line:
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0

print(f"Maximum calories: {max(elves)}")
