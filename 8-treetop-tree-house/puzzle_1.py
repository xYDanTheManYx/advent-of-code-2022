with open("input.txt") as f:
    forest = f.read().split("\n")

tree_rows = [[int(tree) for tree in tree] for tree in [list(tree) for tree in forest]]
visible_trees = 0


def is_tree_visible(tree: int, tree_index: int, row_index: int) -> int:
    visibility_check = 0
    if row_index == 0 or row_index == len(tree_rows)-1 or tree_index == 0 or tree_index == len(tree_rows[0])-1:
        return 1
    else:
        if tree > max(tree_rows[row_index][:tree_index]):
            visibility_check += 1
        if tree > max(tree_rows[row_index][tree_index+1:]):
            visibility_check += 1
        if tree > max([tree[tree_index] for tree in tree_rows][:row_index]):
            visibility_check += 1
        if tree > max([tree[tree_index] for tree in tree_rows][row_index+1:]):
            visibility_check += 1
        return 1 if visibility_check > 0 else 0


for row_index, row_of_trees in enumerate(tree_rows):
    for tree_index, tree in enumerate(row_of_trees):
        visible_trees += is_tree_visible(tree, tree_index, row_index)

print("puzzle 1:", visible_trees)
