from pathlib import Path
from itertools import pairwise
from math import copysign

# Load data
reports = [list(map(int,level.strip('\n').split())) for level in open(Path(__file__).parent / "test.txt")]

# Assignment 1
report_diffs = [[x[1] - x[0] for x in pairwise(report)] for report in reports]
is_safe = [True for diffs in report_diffs if all(1 <= abs(diff) <= 3 and copysign(1.0, diff) == copysign(1.0, diffs[0]) for diff in diffs)]
print(f"Safe Levels: {len(is_safe)}")
