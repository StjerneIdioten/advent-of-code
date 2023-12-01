import sys
import os
import re

if __name__ == "__main__":
    contained_pairs = 0
    overlapping_pairs = 0
    with open(os.path.join(sys.path[0], "data")) as file:
        while (line := file.readline().rstrip()):
            ranges = list(map(int, re.split("[\n,-]+", line)))
            e1, e2 = (ranges[0:2], ranges[2:4])
            
            if max(e1[0], e2[0]) <= min(e1[1], e2[1]):
                overlapping_pairs += 1

            if (min(e1[0], e2[0]) == e2[0]):
                e1, e2 = e2, e1
    
            if (e1[0] == e2[0]) or (e1[1] >= e2[1]) or (e1[0] > e2[0]):
                contained_pairs += 1

    print(f"C: {contained_pairs}, O: {overlapping_pairs}")

            