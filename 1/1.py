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
ordered = sorted(elves)[-3:]

print(f"Maximum calories: {max(elves)}")
print(f"Sum of first three elves: {sum(ordered)}")
