with open("input.txt") as f:
    puzzle_input = f.readlines()


combinations = {"A": ("B", "A", "C"), "B": ("C", "B", "A"), "C": ("A", "C", "B")}
shape_scores = {"A": 1, "B": 2, "C": 3}
total_score = 0


for puzzle_line in puzzle_input:
    score = 0
    shape_1, result = puzzle_line.split()
    if result == "X":
        score += shape_scores[combinations[shape_1][2]]
    elif result == "Y":
        score += 3
        score += shape_scores[shape_1]
    else:
        score += 6
        score += shape_scores[combinations[shape_1][0]]
    total_score += score


print("puzzle 2:", total_score)
