import string

with open("input.txt") as f:
    puzzle_input = f.read().split()

priority = {letter: value for letter, value in zip(string.ascii_letters, range(1, 53))}
total_priority = 0

for puzzle_line in puzzle_input:
    item_split = int(len(puzzle_line) / 2)
    first_compartment = puzzle_line[:item_split]
    second_compartment = puzzle_line[item_split:]
    common_item = set(first_compartment).intersection(set(second_compartment))
    if len(common_item) > 1:
        raise ValueError("More than one common item")
    total_priority += priority[common_item.pop()]


print("puzzle 1:", total_priority)
