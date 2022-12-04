with open("input.txt") as f:
    puzzle_input = f.read().split()

overlaps = 0

for puzzle_line in puzzle_input:
    elf_1, elf_2 = puzzle_line.split(",")
    first_sections = range(int(elf_1.split("-")[0]), int(elf_1.split("-")[1])+1)
    second_sections = range(int(elf_2.split("-")[0]), int(elf_2.split("-")[1])+1)
    if len(set(first_sections).intersection(set(second_sections))) > 0:
        overlaps += 1

print("puzzle 2:", overlaps)
