import string

with open("input.txt") as f:
    puzzle_input = f.read().split()

priority = {letter: value for letter, value in zip(string.ascii_letters, range(1, 53))}
total_priority = 0

for index in range(0, len(puzzle_input), 3):
    group_one, group_two, group_three = puzzle_input[index:index+3]
    badge = set(group_one).intersection(set(group_two).intersection(set(group_three)))
    if len(badge) > 1:
        raise ValueError("More than one common item")
    total_priority += priority[badge.pop()]


print("puzzle 2:", total_priority)
