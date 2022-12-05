import re
from collections import deque, namedtuple
from io import StringIO

import pandas as pd


CrateMovement = namedtuple("CrateMovement", "number_of_crates from_stack to_stack")
stacks = []
crate_movements = []

with open("input.txt") as f:
    match = re.search(r"(?P<crates>(.|\n)*)(\n{2})(?P<instructions>(.|\n)*)", f.read())
    crates = match.group("crates")
    instructions = match.group("instructions")

df = pd.read_fwf(StringIO(crates), header=None, skipfooter=1)

for column in df.columns:
    stacks.append(deque([item.translate(str.maketrans("", "", "[]")) for item in df[column] if not(pd.isnull(item))]))

for instruction in instructions.split("\n"):
    match = re.search(r"move (\b[0-9]+\b) from (\b[0-9]+\b) to (\b[0-9]+\b)", instruction)
    crate_movements.append((CrateMovement(int(match.group(1)), int(match.group(2)), int(match.group(3)))))

for crate_movement in crate_movements:
    for crate in range(crate_movement.number_of_crates):
        stacks[crate_movement.to_stack-1].appendleft(stacks[crate_movement.from_stack-1].popleft())

print("puzzle 1:", "".join([stack[0] for stack in stacks]))
