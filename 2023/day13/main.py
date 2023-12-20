from pathlib import Path
from itertools import (pairwise)
from copy import deepcopy

patterns = [[list(line.rstrip('\n')) for line in pattern.split('\n')] for pattern in open(Path(__file__).parent / "data").read().split('\n\n')]

def find_mirror_in_rows(pattern, previous_value=None):
    for row_idx,pair in enumerate(pairwise(pattern)):
        if (pair[0] == pair[1]):
            lower = row_idx - 1
            upper = row_idx + 2
            equal = True
            while lower >= 0 and upper <= len(pattern) - 1:
                if pattern[upper] != pattern[lower]:
                    equal = False
                    break
                lower -= 1
                upper += 1
            if equal:
                if previous_value is None or previous_value != row_idx + 1:
                    return row_idx + 1
    return 0

def find_smudge_in_rows(pattern, previous_value):
    for i, row in enumerate(pattern):
        for j, c in enumerate(row):
            new_pattern = deepcopy(pattern)
            if c == '.':
                new_pattern[i][j] = '#'
            else:
                new_pattern[i][j] = '.'
            new_value = find_mirror_in_rows(new_pattern, previous_value)
            if new_value != 0 and new_value != previous_value:
                return new_value
    return 0

total_sum = [0, 0]
for pattern_index,pattern in enumerate(patterns):
    pattern_rotated = list(map(list, zip(*reversed(pattern))))
    reflection_idx = [find_mirror_in_rows(pattern), 0]
    if reflection_idx == [0, 0]:
        reflection_idx[1] = find_mirror_in_rows(pattern_rotated)
    total_sum[0] += reflection_idx[0] * 100 + reflection_idx[1]
    new_reflection_idx = [find_smudge_in_rows(pattern, reflection_idx[0]), 0]
    if new_reflection_idx == [0, 0]:
        new_reflection_idx[1] = find_smudge_in_rows(pattern_rotated, reflection_idx[1])
    total_sum[1] += new_reflection_idx[0] * 100 + new_reflection_idx[1]

print(f"Total sum: {total_sum}")
