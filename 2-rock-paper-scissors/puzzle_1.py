with open("input.txt") as f:
    puzzle_input = f.readlines()


shapes = {"X": "A", "Y": "B", "Z": "C"}
winning_combinations = {"X": "C", "Y": "A", "Z": "B"}
shape_scores = {"X": 1, "Y": 2, "Z": 3}
total_score = 0


def result(shape_1, shape_2):
    if shape_1 == shapes[shape_2]:
        return 3
    elif shape_1 == winning_combinations[shape_2]:
        return 6
    return 0


for puzzle_line in puzzle_input:
    score = 0
    shape_1, shape_2 = puzzle_line.split()
    score += result(shape_1, shape_2)
    score += shape_scores[shape_2]
    total_score += score


print("puzzle 1:", total_score)
