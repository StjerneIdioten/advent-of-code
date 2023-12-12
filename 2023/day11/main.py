from pathlib import Path
from re import finditer
from itertools import (accumulate, chain, combinations, pairwise)

def extract_galaxy_rows (expansion=2):
    with open(Path(__file__).parent / "data") as file:
        galaxies = {}
        row = 0
        for line in file:
            found_galaxies = False
            for m in finditer('#',line):
                found_galaxies = True
                galaxies.setdefault(m.start(), []).append(row)
            row += 1 if found_galaxies else expansion

    return sorted(galaxies.items())

def expand_galaxy_columns (galaxies, expansion=2):
    return chain.from_iterable(((r,g[0]) for r in g[1]) for g in map(lambda col,shift: (col[0] + shift, col[1]), galaxies, accumulate(map(lambda x: (x[1][0] - x[0][0] - 1) * (expansion - 1), pairwise(galaxies)), initial=0)))

def manhattan_distance_sum (galaxy_pairs):
    return sum((abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in combinations(galaxy_pairs, 2)))

print(f"Total Distance 1x: {manhattan_distance_sum(expand_galaxy_columns(extract_galaxy_rows(expansion=2), expansion=2))}")
print(f"Total Distance 1000000x: {manhattan_distance_sum(expand_galaxy_columns(extract_galaxy_rows(expansion=1000000), expansion=1000000))}")
