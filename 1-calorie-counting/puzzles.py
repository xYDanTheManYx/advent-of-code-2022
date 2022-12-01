with open("input.txt") as f:
    puzzle_input = f.readlines()

calories = 0
elves_calories = []

for puzzle_line in puzzle_input:
    try:
        calories += int(puzzle_line.strip())
    except ValueError:
        elves_calories.append(calories)
        calories = 0

print("puzzle 1:", max(elves_calories))
print("puzzle 2:", sum(sorted(elves_calories, reverse=True)[:3]))
