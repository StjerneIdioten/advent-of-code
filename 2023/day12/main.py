from pathlib import Path
from functools import cache

# Nice little decorator that does memoisation
@cache
def backtrack(springs, damaged):
    if springs == "":
        return 1 if damaged == () else 0
    if damaged == ():
        return 0 if "#" in springs else 1

    combinations = 0

    if springs[0] in '.?':
        combinations += backtrack(springs[1:], damaged)

    if springs[0] in '#?':
        if damaged[0] <= len(springs) and '.' not in springs[:damaged[0]] and (damaged[0] == len(springs) or springs[damaged[0]] != '#'):
            combinations += backtrack(springs[damaged[0] + 1:], damaged[1:])
    return combinations


total_configs = [0, 0]
with open(Path(__file__).parent / "data") as file:
    while record := file.readline().rstrip('\n').split():
        springs, damaged = record
        damaged = tuple(map(int, record[1].split(',')))
        springs = (springs, '?'.join([springs] * 5))
        damaged = (damaged, damaged * 5)
        total_configs = [total_configs[0] + backtrack(springs[0], damaged[0]),  total_configs[1] + backtrack(springs[1], damaged[1])]

print(f"Configs Folded: {total_configs[0]}, Configs Unfolded: {total_configs[1]}")

