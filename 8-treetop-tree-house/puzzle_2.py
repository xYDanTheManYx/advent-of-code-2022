from functools import reduce


with open("input.txt") as f:
    forest = f.read().split("\n")

tree_rows = [[int(tree) for tree in tree] for tree in [list(tree) for tree in forest]]
highest_scenic_score = 0


def tree_scenic_score(tree: int, tree_index: int, row_index: int) -> int:
    viewing_distances = []
    left_of_tree = tree_rows[row_index][:tree_index]
    left_of_tree.reverse()
    right_of_tree = tree_rows[row_index][tree_index+1:]
    above_tree = [tree[tree_index] for tree in tree_rows][:row_index]
    above_tree.reverse()
    below_tree = [tree[tree_index] for tree in tree_rows][row_index+1:]
    for direction in [left_of_tree, right_of_tree, above_tree, below_tree]:
        for index, neighbouring_tree in enumerate(direction):
            if tree > neighbouring_tree:
                pass
            else:
                viewing_distances.append(index+1)
                break
            if len(direction) == index+1:
                viewing_distances.append(index + 1)
    return reduce(lambda x, y: x*y, viewing_distances) if len(viewing_distances) == 4 else 0


for row_index, row_of_trees in enumerate(tree_rows):
    for tree_index, tree in enumerate(row_of_trees):
        scenic_score = tree_scenic_score(tree, tree_index, row_index)
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

print("puzzle 2:", highest_scenic_score)
