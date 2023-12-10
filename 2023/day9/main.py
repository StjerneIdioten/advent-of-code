from pathlib import Path
from itertools import pairwise

with open(Path(__file__).parent / "data") as file:
    sequences = [list(map(int, line.split())) for line in file.readlines()]

def prediction(sequence):
    if (diff := list(map(lambda x: x[1] - x[0], pairwise(sequence)))) and any(diff):
        return sequence[-1] + prediction(diff)
    return sequence[-1]

print(f"OASIS Report Prediction Result: {sum([prediction(sequence[:: 1]) for sequence in sequences])}")
print(f"OASIS Report History Result:    {sum([prediction(sequence[::-1]) for sequence in sequences])}")
    