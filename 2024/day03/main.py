from pathlib import Path
from itertools import (pairwise, combinations)
from math import copysign

# Load data
reports = [list(map(int,level.strip('\n').split())) for level in open(Path(__file__).parent / "data.txt")]

def is_report_safe(report):
    diffs = [x[1] - x[0] for x in pairwise(report)]
    return all(1 <= abs(diff) <= 3 and copysign(1.0, diff) == copysign(1.0, diffs[0]) for diff in diffs)

# Assignment 1
safe_levels = [True for report in reports if is_report_safe(report)]

# Assignment 2
safe_levels_width_damper = [True for report in reports if any([is_report_safe(report_damped) for report_damped in combinations(report, len(report) - 1)])]
print(f"Safe Levels: {len(safe_levels)}; {len(safe_levels_width_damper)} with damper")