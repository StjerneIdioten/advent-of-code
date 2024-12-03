from pathlib import Path
from collections import Counter

# Assignment 1
left_list, right_list = [sorted(l) for l in zip(*(map(int,row.strip('\n').split()) for row in open(Path(__file__).parent / "data.txt")))]
print(f"Total distance: {sum(abs(x[0] - x[1]) for x in zip(left_list, right_list))}")
# Assignment 2
right_tally = Counter(right_list)
print(f"Similarity score: {sum(right_tally[x] * x for x in left_list)}")
