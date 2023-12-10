from pathlib import Path
from math import lcm

with open(Path(__file__).parent / "data") as file:
    instructions = [0 if c == 'L' else 1 for c in file.readline().rstrip('\n')]
    file.readline()
    nodes = {line[0:3]: (line[7:10], line[12:15]) for line in file.readlines()}
    start_nodes = [node for node in nodes if node.endswith('A')]

def step_cycle(start_node, only_ending = False):
    idx = 0
    next_node = start_node
    steps = 1
    while (next_node := nodes[next_node][instructions[idx]]) and ((only_ending and not next_node.endswith('Z')) or (not only_ending and next_node != 'ZZZ') or steps == 1):
        if (idx := idx + 1) == len(instructions):
            idx = 0
        steps += 1
    return steps

print(f"Steps starting from 'AAA': {step_cycle('AAA')}")
print(f"Steps starting from {start_nodes}: {lcm(*[step_cycle(start_node, start_node) for start_node in start_nodes])}")